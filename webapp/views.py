from django.http import HttpResponse
from django.shortcuts import render
def home(request):
	a=5
	b=6
	c=a+b
	return HttpResponse("HI this is Hello world %s" %c)


# Create your views here.
