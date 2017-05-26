# -*- coding: utf-8 -*-
__author__ = 'umi'
__date__ = '2017/5/21 下午11:23'
from random import Random
import os
from django.core.mail import send_mail
from django.conf import settings

from users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM
# from MxOnline import settings

# settings.configure()
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxOnline.settings")
os.environ.update({"DJANGO_SETTINGS_MODULE": "MxOnline.settings"})

def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "在线注册激活链接"
        email_body = "请点击下面的链接激活你的账户：http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


send_mail('233', '666', EMAIL_FROM, ['408465808@qq.com', 'wangwei101108@foxmail.com'])