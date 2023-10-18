from flask_sqlalchemy import SQLAlchemy
import secrets

db = SQLAlchemy()


def Create_Database(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Root@localhost:3306/moviemanagement'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['JWT_SECRET_KEY'] = 'jwt-secret'


    app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
    app.config['WTF_CSRF_SECRET_KEY'] = secrets.token_urlsafe(16)
    app.config['WTF_CSRF_CHECK_DEFAULT'] = False

    

    #Initialize the database to CreateDatabase
    db.init_app(app)
    with app.app_context():
        db.create_all()