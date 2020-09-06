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
from flask import Response, request
from flask_restful import Resource as Restful_Resource
from dateutil.parser import *
import uuid

from models.Resource import Resource


class ResourcesApi(Restful_Resource):
    def get(self):
        # Retrieves all resources
        resources = Resource.objects.to_json()
        return Response(resources, mimetype="application/json", status=200)

    def post(self):
        # Creates new resource and returns the id if success
        body = request.get_json()

        # manually parse dates and uuid
        body["copyrightInfo"]["publication"] = isoparse(body["copyrightInfo"]["publication"]["$date"])
        body["copyrightInfo"]["update"] = isoparse(body["copyrightInfo"]["update"]["$date"])
        body["uuid"] = uuid.UUID(body["uuid"]["$uuid"])

        resource = Resource(**body)
        resource.save()
        id = resource.id
        return {'id': str(id)}, 201
