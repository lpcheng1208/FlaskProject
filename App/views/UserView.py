from time import sleep

from flask import Blueprint, request, render_template, session

from App.ext import cache

blue = Blueprint("blue", __name__)


@blue.route("/user/", methods=["GET", "POST", "PUT", "DELETE"])
def users():
    if request.method == "GET":
        return render_template("UserRegister.html")

    elif request.method == "POST":
        username = request.form.get("username")
        session["username"] = username

        return "注册成功"

    elif request.method == "PUT":

        username = session.get("username", "not_set")

        return username


@blue.route("/index/")
@cache.cached(timeout=20)
def index():
    sleep(5)

    return "你真是一个小天才"


@blue.before_request
def before():
    print("请求前")


@blue.route("/request/")
def reque():
    print("正在执行视图函数")

    return "hello AOP"
