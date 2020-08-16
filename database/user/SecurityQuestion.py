from mongoengine import *

class SecurityQuestion(EmbeddedDocument):
    id = ObjectIdField()
    question = StringField()
    answer = StringField()