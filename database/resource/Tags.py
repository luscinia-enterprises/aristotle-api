from mongoengine import *

class Tags(EmbeddedDocument):
    subject = StringField()
    gradeLevel = StringField()
    curriculum = StringField()
    majorTopic = ListField(StringField())
    minorTopic = ListField(StringField())
    keywords = ListField(StringField())