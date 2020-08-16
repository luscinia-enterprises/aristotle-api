from mongoengine import *


class Admin(Document):
    id = ObjectIdField()
    key = StringField()
    value = GenericEmbeddedDocumentField()
    values = ListField(GenericEmbeddedDocumentField)
