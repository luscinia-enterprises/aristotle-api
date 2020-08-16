from mongoengine import *

class Course(Document):
    id = ObjectIdField()
    name = StringField()
    gradeLevel = IntField()
    curriculum = StringField()
    subject = StringField()
    teacher = ObjectIdField()
    users = ListField(ObjectIdField())
    lessons = ListField(ObjectIdField())
    created = DateField()
    expires = DateField()