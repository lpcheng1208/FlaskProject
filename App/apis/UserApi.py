import uuid

from flask import request
from flask_restful import Resource, fields, marshal

from App.models import User

user_fields = {
    "name": fields.String(attribute="u_name"),
    "password": fields.String(attribute="u_password"),
    "id": fields.Integer,
}

result_fields = {
    "msg": fields.String,
    "status": fields.String,
    "token": fields.String,
    "data": fields.Nested(user_fields)
}

results_fields = {
    "msg": fields.String,
    "status": fields.String,
    "data": fields.List(fields.Nested(user_fields))
}


class UserResource(Resource):
    def post(self):
        action = request.args.get("action")

        username = request.form.get("username")
        password = request.form.get("password")

        if action == "register":
            user = User()
            user.u_name = username
            user.u_password = password

            if user.save():

                result = {
                    "msg": "ok",
                    "status": "200",
                    "data": user,
                }
                return marshal(result, result_fields)
            else:
                return {"msg": "注册失败"}

        elif action == "login":
            users = User.query.filter(User.u_name == username).all()

            if users:
                user = users[0]
                if user.u_password == password:
                    # 生成一个token
                    token = str(uuid.uuid4())

                    user.u_token = token

                    user.save()

                    result = {
                        "msg": "ok",
                        "status": "200",
                        "token": token,
                        "data": user
                    }
                    return marshal(result, result_fields)
                return {"msg": "用户名或密码错误"}

        return {"msg": "ok"}

    def get(self):
        users = User.query.all()

        result = {
            "msg": "ok",
            "status": "200",
            "data": users
        }
        return marshal(result, results_fields)


class UsersResource(Resource):

    def get(self, id):

        user = User.query.get(id)

        if user:
            result = {
                "msg": "ok",
                "status": "200",
                "data": user
            }
            return marshal(result, result_fields)
        else:
            return {"msg", "not exist"}

    def post(self, id):
        return {"msg": "ok"}

    def patch(self, id):
        return {"msg": "patch ok"}

    def put(self, id):
        user = User.query.get(id)

        username = request.form.get("username")
        password = request.form.get("password")
        if user:
            if username:
                user.u_name = username
            if password:
                user.u_password = password
            user.save()
            return {"msg": "modify success"}
        else:

            return {"msg": "not exist"}

    def delete(self, id):
        user = User.query.get(id)

        if user:
            user.delete()

            return {"msg": "delete ok"}
        else:
            return {"msg": "not exist"}
