# coding: utf8
from __future__ import unicode_literals

from django.db import models



class EmployeeInformation(models.Model):
    name = models.CharField("姓名",max_length=20, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=20, blank=True, null=True)
    post = models.CharField(max_length=20, blank=True, null=True)
    entry_time = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    company = models.CharField(max_length=20, blank=True, null=True)
    project = models.CharField(max_length=20, blank=True, null=True)
    plate = models.CharField(max_length=20, blank=True, null=True)
    count_time = models.DateField(blank=True, null=True)
    foreman = models.FloatField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    household_registration = models.CharField(max_length=20, blank=True, null=True)
    social_security = models.CharField(max_length=20, blank=True, null=True)
    nation = models.CharField(max_length=20, blank=True, null=True)
    political_status = models.CharField(max_length=20, blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    last_degree = models.CharField(max_length=20, blank=True, null=True)
    graduation_time = models.CharField(max_length=20, blank=True, null=True)
    school = models.CharField(max_length=40, blank=True, null=True)
    specialty = models.CharField(max_length=40, blank=True, null=True)
    idnumber = models.CharField(max_length=20, blank=True, null=True)
    contact_address = models.CharField(max_length=100, blank=True, null=True)
    cellphone = models.CharField(max_length=20, blank=True, null=True)
    mailbox = models.CharField(max_length=40, blank=True, null=True)
    emergency_contact = models.CharField(max_length=20, blank=True, null=True)
    relationship = models.CharField(max_length=20, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    work_experience = models.CharField(max_length=200, blank=True, null=True)

    def countnumber(self):
        # return date.today() - self.entrytime
        return '233'
    countnumber.short_description = '2333'
    test = property(countnumber)


    class Meta:
        managed = False
        db_table = 'employee_information'
        verbose_name = '员工信息'
        verbose_name_plural = '员工信息'
