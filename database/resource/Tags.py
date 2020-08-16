from mongoengine import *

class Tags(EmbeddedDocument):
    subject = StringField()
    gradelevel = StringField()
    curriculum = StringField()
    majorTopic = ListField(StringField())
    minorTopic = ListField(StringField())
    keywords = ListField(StringField())