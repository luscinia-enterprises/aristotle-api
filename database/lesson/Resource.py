from mongoengine import *

from database.general import LearningStyle


class Resource(Document):
    resourceId = ObjectIdField()
    learningStyleDelta = EmbeddedDocumentField(LearningStyle)
    performance = IntField()
    response = IntField()
    timesServed = IntField()
    servedScore = IntField()