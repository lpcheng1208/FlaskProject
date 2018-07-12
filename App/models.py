from App.ext import db
from App.utils import BaseModel

PERMISSION_READ = 1
PERMISSION_WRITE = 2


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(16))


class User(db.Model, BaseModel):
    u_token = db.Column(db.String(128))
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(16), unique=True)
    u_password = db.Column(db.String(256))
    is_activate = db.Column(db.Boolean, default=False)
    # 用户权限
    # 权限设计
    # 2 的 n 次方
    # 1 2 4 8 16 32 ...
    # 1 读权限
    # 2 写权限
    # 4 删除
    u_permission = db.Column(db.Integer, default=0)

    def check_permission(self, permission):
        return self.u_permission & permission == permission
