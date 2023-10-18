from flask import Blueprint


m_blp = Blueprint('movies', __name__, url_prefix='/movies')
l_blp = Blueprint('login', __name__, url_prefix='/users')



@m_blp.route('/test')
def Hello():
    return 'Blueprint Working Perfectly'

@l_blp.route('/test')
def Hello():
    return 'Login Blueprint is working'