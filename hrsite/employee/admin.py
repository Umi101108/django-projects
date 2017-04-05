# coding:utf8
from django.contrib import admin

# Register your models here.
from .models import EmployeeInformation



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'department', 'post', 'countnumber', 'test')
    list_display_links = ('name', 'rank')
    search_fields = ['name']
    list_filter = ('rank', 'department')
    fieldsets = [
    	(None, {'fields': ['name']}),
    	('基本信息', {'fields': ['name', 'sex', 'date_of_birth', 'age', 'nation', ('political_status', 'marital_status'), 'household_registration', 'social_security', 'idnumber'],
    					'classes': ['collapse']}),
    	('岗位信息', {'fields': [('company', 'project'), ('department', 'plate'), ('post', 'rank'), ('entry_time', 'count_time'), 'foreman'],
    					'classes': ['collapse']}),
    	('联系方式', {'fields': ['cellphone', 'mailbox', 'contact_address'],
    					'classes': ['collapse']}),
    	('学历信息', {'fields': [('last_degree', 'graduation_time'), ('school', 'specialty')],
    					'classes': ['collapse']}),
    	('工作经历', {'fields': ['work_experience'],
    					'classes': ['collapse']}),
    	('紧急联系人', {'fields': [('emergency_contact', 'relationship'), 'contact_number'],
    					'classes': ['collapse', 'wide']})

    ]

admin.site.register(EmployeeInformation, EmployeeAdmin)
