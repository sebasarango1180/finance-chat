import datetime
#from django.db import models

from djongo import models


class Message(models.Model):

    time_published = models.FloatField(default=datetime.datetime.utcnow().timestamp())
    text = models.TextField()
    user_id = models.ObjectIdField()
    room = models.TextField()
