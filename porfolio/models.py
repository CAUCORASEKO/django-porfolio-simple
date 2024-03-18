from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='porfolio/images/')
    url = models.URLField(blank=True)

    
