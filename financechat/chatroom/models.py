import datetime
# import bson

from djongo import models
# from djongo.base import DjongoClient
from django.contrib.auth.models import User

MESSAGES_TO_DISPLAY = 50

# DjongoClient.enforce_schema = False


class _MessageManager(models.Manager):

    def retrieve(self, room, limit=MESSAGES_TO_DISPLAY):

        return super().filter(room=room)[:limit]


class Message(models.Model):

    _id = models.ObjectIdField()     # default=bson.ObjectId.from_datetime(datetime.datetime.utcnow()))
    time_published = models.FloatField(default=datetime.datetime.utcnow().timestamp())
    text = models.TextField()
    username = models.TextField()
    room = models.TextField()

    objects = _MessageManager()

    class Meta:
        ordering = ['-time_published']


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(max_length=400, blank=True)

