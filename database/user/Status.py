from mongoengine import *

class Status(EmbeddedDocument):
    accountLocked = BooleanField()
    accountSuspended = BooleanField()
    accountBlocked = BooleanField()
    pendingDeletion = BooleanField()
    pendingConfirmation = BooleanField()
    pendingAction = BooleanField()