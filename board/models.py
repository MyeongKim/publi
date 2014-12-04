# coding : utf-8
from django.db import models

# Create your models here.
class Photo(models.Model):
	image_file = models.ImageField(upload_to='static_files/uploaded/original/%Y/%m/%d')
	filtered_image_file = models.ImageField(upload_to='static_files/uploaded/filtered/%Y/%m/%d')
	description = models.TextField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	
	def delete(self,*args,**kargs):
		self.image_file.delete()
		self.filtered_image_file.delete()
		super(Photo.self).delete(*args,**kwargs)

class Categories(models.Model):
	Title = models.CharField(max_length=40, null=False)

	class Admin:
		pass

class TagModel(models.Model):
	Title = models.CharField(max_length=20,null=False)	

class Entries(models.Model):
	Title = models.CharField(max_length=80, null=False)
	Content = models.TextField(null=False)
	created = models.DateTimeField(auto_now_add=True, auto_now=True)
	Comments = models.PositiveSmallIntegerField(default=0,null=True)

	def __unicode__(self):
		return u'%s %s' % (self.Title, self.Content)
	def __str__(self):
		return self.__unicode__()

	class Admin:
		pass	

class Comments(models.Model):
	Name = models.CharField(max_length=20, null=False)
	Password = models.CharField(max_length=32, null=False)
	Content = models.TextField(max_length=2000,null=False)
	created = models.DateTimeField(auto_now_add=True, auto_now=True)

class Users(models.Model):
	Email = models.CharField(max_length=20, null=False)
	Password = models.CharField(max_length=20, null=False)