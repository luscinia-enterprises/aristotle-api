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

import os

from flask import Flask, request, Response
from mongoengine import *
from dateutil.parser import *
import uuid

from models.Resource import Resource

app = Flask('aristotle')
connect(host=os.getenv('MONGODB_URL', 'mongodb://localhost:27017/aristotle'))


@app.route('/resources', methods=['GET'])
def get_resources():
    # Retrieves all resources
    resources = Resource.objects.to_json()
    return Response(resources, mimetype="application/json", status=200)


@app.route('/resources/<resource_id>', methods=['GET'])
def get_resource(resource_id):
    # Retrieves resource by id
    try:
        resource = Resource.objects.get(pk=resource_id)
    except DoesNotExist as e:
        return e, 404
    except MultipleObjectsReturned as e:
        return e, 500
    resource_json = resource.to_json()
    return Response(resource_json, mimetype="application/json", status=200)


@app.route('/resources', methods=['POST'])
def create_resource():
    # Creates new resource and returns the id if success
    body = request.get_json()

    # manually parse dates and uuid
    body["copyrightInfo"]["publication"] = isoparse(body["copyrightInfo"]["publication"]["$date"])
    body["copyrightInfo"]["update"] = isoparse(body["copyrightInfo"]["update"]["$date"])
    body["uuid"] = uuid.UUID(body["uuid"]["$uuid"])

    resource = Resource(**body)
    resource.save()
    return Response("Created", status=201)


@app.route('/resources/<resource_id>', methods=['PUT'])
def update_resource(resource_id):
    # Updates resource by id
    try:
        body = request.get_json()
        resource = Resource.objects.get(pk=resource_id)
    except DoesNotExist:
        return "No resource found", 404
    try:
        # manually parse dates and uuid if needed
        if "copyrightInfo" in body and "publication" in body["copyrightInfo"]:
            body["copyrightInfo"]["publication"] = isoparse(body["copyrightInfo"]["publication"]["$date"])
        if "copyrightInfo" in body and "update" in body["copyrightInfo"]:
            body["copyrightInfo"]["update"] = isoparse(body["copyrightInfo"]["update"]["$date"])
        if "uuid" in body:
            body["uuid"] = uuid.UUID(body["uuid"]["$uuid"])

        resource.update(**body)
    except InvalidQueryError:
        return "Bad request", 400
    return "Updated", 200


@app.route('/resources/<resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    # Deletes resource by id
    try:
        resource = Resource.objects.get(pk=resource_id)
    except DoesNotExist as e:
        return e, 404
    except MultipleObjectsReturned as e:
        return e, 500
    resource.delete()
    return "Deleted", 200


if __name__ == '__main__':
    app.run(debug=True)
