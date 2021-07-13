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

from .resource import *
from .root import *
from .student import *


def initialize_routes(api):
    api.add_resource(Root, '/')
    api.add_resource(HealthCheck, '/health')
    api.add_resource(Resources, '/resources')
    api.add_resource(ResourceLearningStyles, '/resources/learningstyles')
    api.add_resource(ResourceById, '/resources/<resource_id>')
    api.add_resource(StudentLearningStyleById, '/students/<student_id>/learningstyle')
    api.add_resource(Students, '/students')
