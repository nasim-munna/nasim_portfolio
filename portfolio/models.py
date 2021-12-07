from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.urls import reverse

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/',blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio:blog_details", kwargs={
            "slug": self.slug
            })

class Work(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='blog/',blank=True)
    url = models.URLField()
    category = models.CharField(max_length=20,blank=True)


    def __str__(self):
        return self.title

class Cv(models.Model):
    cv = models.FileField(upload_to='cv/',blank=True)

class Client(models.Model):
    image = models.ImageField(upload_to='client/',blank=True)
    url = models.URLField()

class Testimonial(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='testimonial/',blank=True)
    designation = models.CharField(max_length=30)
    comment = models.TextField()



    

