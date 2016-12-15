# coding:utf8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	string = u"好好学习Django，用它来建网站"
	TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
	info_dict = {'site': u'haohaoxuexi', 'content': u'tiantianxiangshang'}
	List = map(str, range(100))
	num = 60
	return render(request, 'home.html', {'string':string, 'TutorialList': TutorialList, 'info_dict':info_dict, 'List':List, 'num':num})

def add(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))