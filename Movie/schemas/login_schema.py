from marshmallow import Schema, fields


class Login_Schema(Schema):

    id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()


login = Login_Schema()
users = Login_Schema(many=True)