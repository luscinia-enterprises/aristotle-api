from mongoengine import *


class LearningStyle(EmbeddedDocument):
    llss = IntField()
    slss = IntField()
    alss = IntField()
    klss = IntField()
    mlss = IntField()
    sms = IntField()
    qms = IntField()
    tms = IntField()