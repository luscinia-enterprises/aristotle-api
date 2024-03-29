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


class Root(Restful_Resource):
    def get(self):
        # Health check
        return Response(status=200)


class HealthCheck(Restful_Resource):
    def get(self):
        # Health check
        return Response(status=200)
