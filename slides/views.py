from django.shortcuts import render

from KISS.common import rtr

def defaultscreen (request):
	from slides.models import Slide

	c = {}

	c['slide'] = Slide.objects.all()[0]

	return rtr ("slide.html", c, request)
