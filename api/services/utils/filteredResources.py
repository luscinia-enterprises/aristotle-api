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

import json


def filterResources(resources):
    json_resources = json.loads(resources)
    filtered_resources = []
    for resource in json_resources:
        filtered_resources.append(
            {
                "_id": resource['_id'],
                "learningStyle": resource['learningStyle']
            })
    return filtered_resources
