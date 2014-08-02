from django.db import models

# Create your models here.

class Slide (models.Model):
	title = models.CharField (max_length=200)
	created_date = models.DateTimeField('date created')
	html = models.TextField ()

	def __unicode__(self):
		return "#" + unicode(self.pk) + " " + self.title

