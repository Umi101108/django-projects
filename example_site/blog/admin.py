# coding: utf8
from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	list_filter = ('status', 'created', 'publish', 'author')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}	# 自动根据title生成slug
	raw_id_fields = ('author',)	# 新增post时author显示为一个搜索控件
	date_hierarchy = 'publish'	# 时间层快速导航
	ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)