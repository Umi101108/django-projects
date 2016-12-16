from django.contrib import admin
from .models import Article, Person

# Register your models here.
# admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'pub_date', 'update_time',)

class PersonAdmin(admin.ModelAdmin):
	list_display = ('full_name','age')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
