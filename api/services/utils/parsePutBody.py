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

import uuid

from dateutil.parser import isoparse


def parsePutBody(body):
    # manually parse dates and uuid if needed
    if "copyrightInfo" in body and "publication" in body["copyrightInfo"]:
        body["copyrightInfo"]["publication"] = isoparse(body["copyrightInfo"]["publication"]["$date"])
    if "copyrightInfo" in body and "update" in body["copyrightInfo"]:
        body["copyrightInfo"]["update"] = isoparse(body["copyrightInfo"]["update"]["$date"])
    if "uuid" in body:
        body["uuid"] = uuid.UUID(body["uuid"]["$uuid"])
