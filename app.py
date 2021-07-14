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

from flask import Flask
from flask_restful import Api
from mongoengine import *
from api.controller.__init__ import initialize_routes
from api.services.utils.cache import cache

app = Flask('aristotle')
api = Api(app)
connect(host=os.getenv('MONGODB_URL', 'mongodb://localhost:27017/aristotle'))

config = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_REDIS_HOST': os.getenv('REDIS_HOST', 'localhost'),
    'CACHE_REDIS_PORT': os.getenv('REDIS_PORT', '6379')}
cache.init_app(app, config= config)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
