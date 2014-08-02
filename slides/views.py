from django.shortcuts import redirect, get_object_or_404

from KISS.common import rtr
from slides.models import Screen, Slide

def screens (request):

	c = {}
	c['screens'] = Screen.objects.all()

	return rtr ("screens.html", c, request)

def index (request):
	c = {}

	if request.session.get('selected', False):
		try:
			screen = get_object_or_404 (Screen, pk=request.session['screen'])
		except:
			return redirect ('screens')
		c['slide'] = Slide.objects.filter(screen=screen)[1]
		c['screen'] = screen.name
		return rtr ("slide.html", c, request)
		
	else:
		return redirect ('screens')



def screen (request, screen):
	screen = get_object_or_404 (Screen, pk=screen)
	request.session['screen'] = screen.pk
	request.session['selected'] = True
	return redirect ('index')
