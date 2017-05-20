# -*- coding: utf-8 -*-
__author__ = 'umi'
__date__ = '2017/5/18 上午12:47'

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)