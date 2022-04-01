from django.db import models

from thumbnails.fields import ImageField


# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=250, blank=True)
    nationality = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=250, blank=True, unique=True)
    doc_id = models.CharField(max_length=250, blank=True, unique=True)
    face_id = models.CharField(max_length=250, blank=True)
    data = models.CharField(max_length=10000, blank=True)
    face = ImageField(upload_to='static/images', blank=True, pregenerated_sizes=["large", "medium"])
    face_tmp = ImageField(upload_to='static/images', blank=True, pregenerated_sizes=["large", "medium"])
    it2 = models.CharField(max_length=10000, blank=True)
