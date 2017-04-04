from __future__ import unicode_literals

from django.db import models

# Create your models here.

class EmployeeInformation(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_information'

    def __unicode__(self):
        return self.name
