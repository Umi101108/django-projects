# -*- coding: utf-8 -*-
__author__ = 'umi'
__date__ = '2017/5/22 下午11:54'

from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM
import os


os.environ.update({"DJANGO_SETTINGS_MODULE": "MxOnline.settings"})

send_mail('233', '666', EMAIL_FROM, ['408465808@qq.com', 'wangwei101108@foxmail.com'])
m
