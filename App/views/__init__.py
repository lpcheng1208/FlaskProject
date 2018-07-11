from App.views.OrderView import order
from App.views.UserView import blue


# 懒加载, 后初始化方式
def init_blueprint(app):
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(blueprint=order)
