from django.db import models

# Create your models here.

class Slide (models.Model):
	title = models.CharField (max_length=200)
	created_date = models.DateTimeField('date created', auto_now_add=True)
	html = models.TextField ()

	def __unicode__(self):
		return "#" + unicode(self.pk) + " " + self.title



class Screen (models.Model):
	name = models.CharField (max_length=200)
	description = models.TextField ()
	slides = models.ManyToManyField (Slide)

	def __unicode__(self):
		return self.name

