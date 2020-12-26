from mongoengine import *
import datetime

class Chat(Document):
    user = StringField(required=True)
    message = StringField(required=True)
    time = DateTimeField(default=datetime.datetime.utcnow)


