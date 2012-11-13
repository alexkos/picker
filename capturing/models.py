from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Site(models.Model):
	url  = models.CharField(max_length=100)
	user = models.ForeignKey(User)

class TextSite(models.Model):
	url   = models.CharField(max_length=100)
	title = models.CharField(max_length=200)
	text  = models.TextField()
	site  = models.ForeignKey(Site)