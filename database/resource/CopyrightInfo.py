from mongoengine import *

class CopyrightInfo(EmbeddedDocument):
    url = StringField()
    author = StringField()
    publisher = StringField()
    publication = DateField()
    update = DateField()
    location = StringField()
