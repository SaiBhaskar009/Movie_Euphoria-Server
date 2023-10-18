from extensions import CORS, JWT, CSRF
from flask_restful import Api


def create_api(app):

    api = Api(app)

    for extensions in (
        CSRF,
        JWT,
        CORS
    ):
        extensions.init_app(app)
    
    return api

