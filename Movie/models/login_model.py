from default_settings import db 


class Login(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255),nullable=False, unique=True)
    password = db.Column(db.String(255),nullable=False)



    def __init__(self, username, email, password):

        self.username = username,
        self.email= email,
        self.password = password

