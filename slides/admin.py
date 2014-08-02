from django.contrib import admin

from slides.models import Slide, Screen

class SlideAdmin (admin.ModelAdmin):
	change_form_template = 'admin_change_form.html'




admin.site.register (Slide, SlideAdmin)
admin.site.register (Screen)
