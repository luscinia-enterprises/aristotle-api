from mongoengine import *

from database.general.LearningStyle import LearningStyle
from database.resource.CopyrightInfo import CopyrightInfo
from database.resource.Tags import Tags


class Resource(Document):
    _class = StringField()
    uuid = UUIDField()
    name = StringField()
    content = StringField()
    learningStyle = EmbeddedDocumentField(LearningStyle)
    copyrightInfo = EmbeddedDocumentField(CopyrightInfo)
    tags = EmbeddedDocumentField(Tags)
    meta = {'collection': 'resources'}
