from django.db import models

class Notices(models.Model):
	title = models.CharField(max_length = 140)	
	body = models.TextField()
		
	def __unicode__(self):
		return self.title
		
	def __str__(self):
		return self.title
