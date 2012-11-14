from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class NewSites(models.Model):
    url  = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.url

class TextSite(models.Model):
    url   = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text  = models.TextField()
    site  = models.ForeignKey(NewSites)

    def __unicode__(self):
        return self.url