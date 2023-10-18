from default_settings import db

class Movie(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Name =  db.Column(db.String(255), nullable=False)
    Genre = db.Column(db.String(255), nullable=False)
    Released= db.Column(db.Date, nullable=False)
    OTT = db.Column(db.String(255), nullable=False)



    def __init__(self,Name,Genre,Released,OTT):

       self.Name = Name
       self.Genre = Genre
       self.Released =Released
       self.OTT =OTT


