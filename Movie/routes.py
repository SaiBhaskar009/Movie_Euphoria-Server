from flask_restful import Api
from views.movie_views import Movie_Requirements
from views.auth import User_login


def Create_routes(app):

    api = Api()


    api.add_resource(Movie_Requirements, '/movies', methods = ['GET','POST','DELETE'])
    api.add_resource(User_login, '/users', methods = ['GET','POST','PUT','DELETE'])


    api.init_app(app)