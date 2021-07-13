#  Aristotle Learning Platform: Luscinia Enterprises Assn.
#  Copyright (C) 2021
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

from flask import Response
from flask_restful import Resource as Restful_Resource
from mongoengine import *

from api.models.User import User


class Students(Restful_Resource):
    # Retrieves all students
    def get(self):
        users = User.objects.to_json()
        return Response(users, mimetype="application/json", status=200)


class StudentLearningStyleById(Restful_Resource):
    # Retrieves learningstyle by student id
    def get(self, student_id):
        try:
            user = User.objects.get(pk=student_id)
        except DoesNotExist:
            return "No student found", 404
        except MultipleObjectsReturned:
            return "Multiple objects returned. Database error. (This should never happen)", 500

        learningstyle = user.learningStyle.to_json()

        return Response(learningstyle, mimetype="application/json", status=200)
