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

from mongoengine import *

from models.general.LearningStyle import LearningStyle
from models.resource.CopyrightInfo import CopyrightInfo
from models.resource.Tags import Tags


class Resource(Document):
    _class = StringField(required=True)
    content = StringField(required=True)
    copyrightInfo = EmbeddedDocumentField(CopyrightInfo, required=True)
    learningStyle = EmbeddedDocumentField(LearningStyle, required=True)
    name = StringField(required=True)
    tags = EmbeddedDocumentField(Tags, required=True)
    uuid = UUIDField(binary=True, required=True)
    meta = {'collection': 'resources'}

