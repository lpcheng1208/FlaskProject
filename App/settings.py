def get_db_uri(dbinfo):
    # 提供默认值
    DB = dbinfo.get("DB") or "mysql"
    DRIVER = dbinfo.get("DRIVER") or "pymysql"
    USER = dbinfo.get("USER") or "stu"
    PASSWORD = dbinfo.get("PASSWORD") or "Lpcheng1208-"
    HOST = dbinfo.get("HOST") or "localhost"
    PORT = dbinfo.get("PORT") or "3306"
    NAME = dbinfo.get("NAME") or "mysql"

    return "{}+{}://{}:{}@{}:{}/{}".format(DB, DRIVER, USER, PASSWORD, HOST, PORT, NAME)


class Config:
    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "lpc1208"


class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        "USER": "stu",
        "PASSWORD": "Lpcheng1208-",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flaskproject",
        "DB": "mysql",
        "DRIVER": "pymysql",

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

    SESSION_TYPE = "redis"


class TestingConfig(Config):
    DEBUG = True

    DATABASE = {
        "USER": "stu",
        "PASSWORD": "Lpcheng1208-",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flaskproject",
        "DB": "mysql",
        "DRIVER": "pymysql",

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StatingConfig(Config):
    DEBUG = True

    DATABASE = {
        "USER": "stu",
        "PASSWORD": "Lpcheng1208-",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flaskproject",
        "DB": "mysql",
        "DRIVER": "pymysql",

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DEBUG = True

    DATABASE = {
        "USER": "stu",
        "PASSWORD": "Lpcheng1208-",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flaskproject",
        "DB": "mysql",
        "DRIVER": "pymysql",

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "stating": StatingConfig,
    "product": ProductConfig,
    "default": DevelopConfig,
}
