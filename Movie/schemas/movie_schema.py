from marshmallow import Schema, fields


class Movie_Schema(Schema):
    id = fields.Int()
    Name = fields.Str(required=True)
    Genre = fields.Str(required=True)
    Released= fields.Date()
    OTT= fields.Str(required=True)


movie = Movie_Schema()
movies = Movie_Schema(many=True)