from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
#MVC Model View Controller

class Status(models.Model):
	content = models.TextField(max_length=300)
	username = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)


	def __unicode__(self):
		return self.content

	def get_absolute_url(self):
		return reverse("status:search",kwargs={"id":self.id})
		#return "/search/%s/"%(self.id)