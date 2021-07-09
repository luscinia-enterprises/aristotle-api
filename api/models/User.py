#  Aristotle Learning Platform: Luscinia Enterprises Assn.
#  Copyright (C) 2020
#      1261612 B.C. LTD.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from mongoengine import *

from api.models.general.LearningStyle import LearningStyle
from api.models.user.LoginRecord import LoginRecord
from api.models.user.SecurityQuestion import SecurityQuestion
from api.models.user.Status import Status


class User(Document):
    preferredName = StringField()
    firstName = StringField()
    middleName = StringField()
    lastName = StringField()
    school = StringField()
    courses = ListField(StringField())
    teachers = ListField(StringField())
    parents = ListField(StringField())
    students = ListField(StringField())
    classicGradeLevel = IntField()
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
    uuid = UUIDField(binary=True)
    _class = StringField()
    meta = {'collection': 'users'}


