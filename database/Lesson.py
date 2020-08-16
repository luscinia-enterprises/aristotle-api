from mongoengine import *

from database.lesson.Resource import Resource
from database.lesson.StudentPerformance import StudentPerformance
from database.resource.Tags import Tags


class Lesson(Document):
    id = ObjectIdField()
    courseId = ObjectIdField()
    resources = ListField(Resource)
    students = ListField(ObjectIdField())
    studentPerformance = ListField(StudentPerformance)
    tags = EmbeddedDocumentField(Tags)
    overallPerformance = IntField()
    overallResponse = IntField()
