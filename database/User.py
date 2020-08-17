import json
from mongoengine import *

from database.general.LearningStyle import LearningStyle
from database.user.LoginRecord import LoginRecord
from database.user.SecurityQuestion import SecurityQuestion
from database.user.Status import Status


class User(Document):
    id = ObjectIdField()
    preferredName = StringField()
    firstName = StringField()
    middleName = StringField()
    lastName = StringField()
    school = StringField()
    courses = ListField(StringField())
    teachers = ListField(StringField())
    parents = ListField(StringField())
    students = ListField(StringField())
    accountCreated = DateTimeField()
    dateOfBirth = DateTimeField()
    email = StringField()
    phone = StringField()
    password = StringField()
    roles = ListField(StringField())
    enabled = BooleanField()
    status = EmbeddedDocumentField(Status)
    passwordResetKey = StringField()
    passwordChange = DateTimeField()
    securityQuestions = EmbeddedDocumentListField(SecurityQuestion)
    loginRecords = EmbeddedDocumentListField(LoginRecord)
    use2FA = BooleanField()
    method2FA = StringField()
    secret2FA = StringField()
    learningStyle = EmbeddedDocumentField(LearningStyle)


