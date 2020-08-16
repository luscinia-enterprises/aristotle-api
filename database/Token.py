from mongoengine import *


class Token(Document):
    id = ObjectIdField()
    username = StringField()
    series = StringField()
    tokenValue = StringField()
    date = DateTimeField()
