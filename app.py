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
