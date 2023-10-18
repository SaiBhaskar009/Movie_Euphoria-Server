from flask_wtf import CSRFProtect


csrf = CSRFProtect()


def init_app(app):
    csrf.init_app(app)