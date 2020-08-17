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
import json

from flask import Flask, jsonify
from mongoengine import *

from database.Resource import Resource

app = Flask('aristotle')
connect(host=os.getenv('MONGODB_URL', 'mongodb://localhost:27017/aristotle'))


@app.route('/', methods=['POST', 'GET', 'PUT', 'DELETE'])
def index():
    return jsonify({'response': 'Hello world!'})


@app.route('/resource/<resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = Resource.objects().get(pk=resource_id)
    resource_json = resource.to_json()
    return resource_json


app.run()
