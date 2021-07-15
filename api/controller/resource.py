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

from flask import Response, request
from flask_restful import Resource as Restful_Resource
from mongoengine import *

from api.models.Resource import Resource
from ..services.utils.cache import cache
from ..services.utils.filteredResources import filterResources
from ..services.utils.parsePostBody import parsePostBody
from ..services.utils.parsePutBody import parsePutBody


class Resources(Restful_Resource):
    def get(self):
        # Retrieves all resources
        resources = Resource.objects.to_json()
        return Response(resources, mimetype="application/json", status=200)

    def post(self):
        # Creates new resource and returns the id if success
        body = request.get_json()

        parsePostBody(body)

        resource = Resource(**body)
        resource.save()
        id = resource.pk
        return {'_id': str(id)}, 201


class ResourceById(Restful_Resource):
    def get(self, resource_id):
        # Retrieves resource by id
        try:
            resource = Resource.objects.get(pk=resource_id)
        except DoesNotExist:
            return "Resource not found", 404
        except MultipleObjectsReturned:
            return "Multiple objects returned. Database error. (This should never happen)", 500
        resource_json = resource.to_json()
        return Response(resource_json, mimetype="application/json", status=200)

    def put(self, resource_id):
        # Updates resource by id
        try:
            body = request.get_json()
            resource = Resource.objects.get(pk=resource_id)
        except DoesNotExist:
            return "No resource found", 404
        try:
            parsePutBody(body)

            resource.update(**body)
        except InvalidQueryError:
            return "Bad request", 400
        return "Updated", 200

    def delete(self, resource_id):
        # Deletes resource by id
        try:
            resource = Resource.objects.get(pk=resource_id)
        except DoesNotExist:
            return "Resource not found", 404
        except MultipleObjectsReturned:
            return "Multiple objects returned. Database error. (This should never happen)", 500
        resource.delete()
        return "Deleted", 200


class ResourceLearningStyles(Restful_Resource):
    # Retrieves all resources filtered to only id and learningstyle
    def get(self):
        resources = Resource.objects.to_json()
        filtered_resources = filterResources(resources)

        return filtered_resources, 200
