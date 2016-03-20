from __future__ import unicode_literals

from django.db import models

# Create your models here.
def content_file_name(instance, filename):
	return '/'.join([filename])
class Page(models.Model):
	highlight = models.CharField(max_length=100,blank=False)
	content = models.TextField(max_length=500,blank=False)
	date = models.DateField(auto_now_add = True,auto_now=False)
	updated = models.DateField(auto_now_add = False,auto_now=True)
	photo = models.FileField(upload_to=content_file_name,default='/placeholder.jpg')

	def __unicode__(self):
		return self.highlight