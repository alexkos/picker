from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class CreateSiteManager(models.Manager):
    def create_site(self, url, user):
        new_site = NewSites.objects.create(url=url, user=user)
        new_site.save()

class NewSites(models.Model):
    url  = models.URLField(max_length=100)
    user = models.ForeignKey(User)

    objects = CreateSiteManager()

    def __unicode__(self):
        return self.url

class TextSite(models.Model):
    url   = models.URLField(max_length=100)
    title = models.CharField(max_length=200)
    text  = models.TextField()
    site  = models.ForeignKey(NewSites)

    def __unicode__(self):
        return self.url
