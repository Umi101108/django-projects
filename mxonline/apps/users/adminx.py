#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-27 21:25:11
# @Author  : Umi (wangwei101108@foxmail.com)
# @Link    : http://umi101108.com
# @Version : $Id$

import os
import xadmin
from xadmin import views

from .models import UserProfile, EmailVerifyRecord, Banner

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "后台管理系统"
    site_footer = "上海天同房地产开发有限公司"
    menu_style = "accordion"

class UserProfileAdmin(object):
    pass

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type']
    search_fields = ['code', 'email']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index' ]
    list_display = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
