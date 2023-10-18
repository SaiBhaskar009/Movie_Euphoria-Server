from flask import Flask
from extensions import create_api
from routes import Create_routes
from default_settings import Create_Database


def Create_Server():

    app = Flask(__name__)
    create_api(app)
    Create_Database(app)
    Create_routes(app)

    from blueprints import m_blp,l_blp
    app.register_blueprint(m_blp)
    app.register_blueprint(l_blp)

    return app

APP = Create_Server()


if __name__ == '__main__':
    APP.run(debug=True)




