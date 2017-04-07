# coding: utf8
from __future__ import unicode_literals

from django.db import models



class EmployeeInformation(models.Model):
    name = models.CharField("姓名", max_length=20, blank=True, null=True)
    rank = models.IntegerField("职级", blank=True, null=True)
    department = models.CharField("部门", max_length=20, blank=True, null=True)
    post = models.CharField("岗位", max_length=20, blank=True, null=True)
    entry_time = models.DateField("入职时间", blank=True, null=True)
    sex = models.CharField("性别", max_length=1, blank=True, null=True)
    company = models.CharField("公司", max_length=20, blank=True, null=True)
    project = models.CharField("项目", max_length=20, blank=True, null=True)
    plate = models.CharField("板块", max_length=20, blank=True, null=True)
    count_time = models.DateField("统计时间", blank=True, null=True)
    foreman = models.FloatField("司龄", blank=True, null=True)
    date_of_birth = models.DateField("出生日期", blank=True, null=True)
    age = models.FloatField("年龄", blank=True, null=True)
    household_registration = models.CharField("户籍地", max_length=20, blank=True, null=True)
    social_security = models.CharField("社保", max_length=20, blank=True, null=True)
    nation = models.CharField("民族", max_length=20, blank=True, null=True)
    political_status = models.CharField("政治面貌", max_length=20, blank=True, null=True)
    marital_status = models.CharField("婚姻状态", max_length=20, blank=True, null=True)
    last_degree = models.CharField("最后学历", max_length=20, blank=True, null=True)
    graduation_time = models.CharField("毕业时间", max_length=20, blank=True, null=True)
    school = models.CharField("毕业学校", max_length=40, blank=True, null=True)
    specialty = models.CharField("专业", max_length=40, blank=True, null=True)
    idnumber = models.CharField("身份证号", max_length=20, blank=True, null=True)
    contact_address = models.CharField("联系地址", max_length=100, blank=True, null=True)
    cellphone = models.CharField("手机号码", max_length=20, blank=True, null=True)
    mailbox = models.CharField("邮箱", max_length=40, blank=True, null=True)
    emergency_contact = models.CharField("紧急联系人", max_length=20, blank=True, null=True)
    relationship = models.CharField("关系", max_length=20, blank=True, null=True)
    contact_number = models.CharField("联系号码", max_length=20, blank=True, null=True)
    work_experience = models.CharField("工作经历", max_length=200, blank=True, null=True)

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

class VacationRecord(models.Model):
    employee = models.ForeignKey(EmployeeInformation)
    vacation_type = models.CharField(max_length=20, blank=True, null=True)
    vacation_time = models.DateField(blank=True, null=True)
    vacation_days = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacation_record'

