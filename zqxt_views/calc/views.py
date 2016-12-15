from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def add(request):
	a = request.GET.get('a',0)
	b = request.GET.get('b',99)
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))


def index(request):
	return render(request, 'home.html')

def old_add2_redirect(request, a, b):
	return HttpResponseRedirect(
		reverse('add2', args=(a, b))
		)