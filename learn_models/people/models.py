from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	mobile = models.CharField(max_length=11)

	def __unicode__(self):
		return self.name