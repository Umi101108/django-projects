from django.contrib import admin

# Register your models here.
from .models import EmployeeInformation



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ['name']

admin.site.register(EmployeeInformation, EmployeeAdmin)
