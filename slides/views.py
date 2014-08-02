from django.shortcuts import render

from KISS.common import rtr

def defaultscreen (request):


	c = {}

	return rtr ("slide.html", c, request)
