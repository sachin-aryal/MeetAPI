from django.db import models

# Create your models here.

class MeetInfo(models.Model):
    message = models.TextField()
    phoneNumber = models.TextField()