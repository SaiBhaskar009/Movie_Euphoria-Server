from flask_restful import Resource
from flask import json, jsonify, request
from default_settings import db 
from blueprints import m_blp
from models.movie_model import Movie
from schemas.movie_schema import movie, movies
from flask_jwt_extended import jwt_required, get_jwt_identity


class Movie_Requirements(Resource):

    @m_blp.route('/getallmovies', methods=['GET'])
    def getallmovies():
        movies_list = Movie.query.all()
        result = movies.dump(movies_list)
        return jsonify(result)
    
    @m_blp.route('/add', methods=['POST'])
    #@jwt_required()
    def addmovie():
        movie_add = Movie(
            Name = request.json['Name'],
            Genre = request.json['Genre'],
            Released= request.json['Released'],
            OTT= request.json['OTT']
        )
        db.session.add(movie_add)
        db.session.commit()
        result = movie.dump(movie_add)
        return jsonify('The Movies is now available', result)

    @m_blp.route('/getmovie/<Name>', methods=['GET'])
    @jwt_required()
    def getmovie(Name):

        get_movie = Movie.query.filter_by(Name=Name).first()
        result = movie.dump(get_movie)
        return jsonify(result)
    
    @m_blp.route('/getbyyear/<year>', methods=['GET'])
    @jwt_required()
    def getbyyear(year):

        get_movie_by_year = Movie.query.filter_by(db.extract('year', Movie.Released)== year).all()
        result = movie.dump(get_movie_by_year)
        return jsonify(result)
    
    @m_blp.route('/getbygenre/<Genre>', methods=['GET'])
    @jwt_required()
    def getbygenre(Genre):

        getby_genre = Movie.query.filter_by(Genre=Genre).all()
        result = movies.dump(getby_genre)
        return jsonify(result)
    
    @m_blp.route('/getbyOTT/<OTT>', methods=['GET'])
    @jwt_required()
    def getbyOTT(OTT):

        getby_OTT = Movie.query.filter_by(OTT=OTT).all()
        result = movie.dump(getby_OTT)
        return jsonify(result)
    
    @m_blp.route('/deletebyname/<Name>', methods=['DELETE'])
    @jwt_required()
    def delete(Name):

        delete_movie = Movie.query.filter_by(Name=Name).first()
        db.session.delete(delete_movie)
        db.session.commit()
        return jsonify({'The Movie is Deleted'})
    
    
    @m_blp.route('/deletebyid/<int:id>', methods=['DELETE'])
    @jwt_required()
    def delete_movie_by_id(id):

        delete_movie = Movie.query.filter_by(id=id).first()
        db.session.delete(delete_movie)
        db.session.commit()
        

    @m_blp.route('/deleteallmovies', methods=['DELETE'])
    @jwt_required()
    def deleteallmovies():
        delete = Movie.query.all()
        db.session.delete(delete)
        db.session.commit()

    
        
       
    
    