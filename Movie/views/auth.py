from models.login_model import Login
from schemas.login_schema import login, users
from default_settings import db 
from flask import request, json, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from blueprints import l_blp
import datetime


class User_login(Resource):

    @l_blp.route('/login', methods=['POST'])
    def login():

       
        username = request.json.get('username')
        password = request.json.get('password')

        post = Login.query.filter_by(username=username).first()

        expires = datetime.timedelta(minutes=3600)

        if post and password == post.password:
           access_token = create_access_token(identity=username, expires_delta=expires)
           return jsonify(access_token)
        else:
           return jsonify('User not found'), 401
        

    @l_blp.route('/register', methods=['POST'])
    def register():
        new_user = Login(
            username = request.json['username'],
            password = request.json['password'],
            email = request.json['email'],
        )
        db.session.add(new_user)
        db.session.commit()
        result = login.dump(new_user)
        return jsonify({
            "Successfully Added New User": result
        })
    
    @l_blp.route('/getallusers', methods=['GET'])
    #@jwt_required()
    def getallusers():
        logined_users = Login.query.all()
        result = users.dump(logined_users)
        return jsonify(result)
    

