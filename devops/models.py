from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
	username = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)

	def __unicode__(self):
		return self.username


class Services(models.Model):
	service = models.CharField(max_length=50)

	def __unicode__(self):
		return self.service


class Host(models.Model):
	hostname = models.CharField(max_length=50)
	ip = models.GenericIPAddressField()
	type = models.CharField(max_length=10)
	os = models.CharField(max_length=50, blank=True, null=True)
	services = models.ManyToManyField(Services)
	note = models.CharField(max_length=500, blank=True, null=True)



