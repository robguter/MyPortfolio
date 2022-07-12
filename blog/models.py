from django.db import models
from django.db.models.fields import CharField, TextField, DateField
import datetime
from django.db.models.fields.files import ImageField

class Post(models.Model):
    title = CharField(max_length=100)
    description = TextField()
    image = ImageField(upload_to='blog/images')
    date = DateField(datetime.date.today)
