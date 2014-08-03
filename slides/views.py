from django.shortcuts import redirect, get_object_or_404, render

from slides.models import Screen, Slide

def screens (request):

	c = {}
	c['screens'] = Screen.objects.all()

	return render (request, "screens.html", c)

def index (request):

	from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

	c = {}

	if request.session.get('selected', False):
		try:
			screen = get_object_or_404 (Screen, pk=request.session['screen'])
		except:
			return redirect ('screens')
		
#		try:
		screenslides = screen.slides.all()
#		except:
#			return redirect ('screens')

		pages = Paginator(screenslides, 1)

			
		page = request.session.get('page')
		try:
			slide = pages.page(page)[0]
			nextpage = page + 1
		except PageNotAnInteger:
			slide = pages.page(1)[0]
			nextpage = 2
		except EmptyPage:
			slide = pages.page(1)[0]
			nextpage = 2

		request.session['page'] = nextpage
		c['page'] = nextpage
				
		c['slide'] = slide

		c['screen'] = screen.name
		return render (request, "slide.html", c)
		
	else:
		return redirect ('screens')



def screen (request, screen):
	screen = get_object_or_404 (Screen, pk=screen)
	request.session['screen'] = screen.pk
	try:
		del request.session['page']
	except:
		pass
	request.session['selected'] = True
	return redirect ('index')
