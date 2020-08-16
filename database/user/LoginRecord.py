from mongoengine import *

class LoginRecord(EmbeddedDocument):
    id = ObjectIdField()
    eventTime = DateTimeField()
    requestAddress = StringField()
    deviceType = StringField()
    location = StringField()