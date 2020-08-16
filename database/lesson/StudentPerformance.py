from mongoengine import *

from database.general import LearningStyle


class StudentPerformance(Document):
    studentId = ObjectIdField()
    learningStyleDelta = EmbeddedDocumentField(LearningStyle)
    performance = IntField()
    response = IntField()