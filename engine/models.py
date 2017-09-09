from django.contrib.auth.models import User
from django.db import models


import uuid
from django.db import models


class Movie(models.Model):
    movieId=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=1000,blank=True)
    genres=models.CharField(max_length=1000,blank=True)
    year=models.IntegerField(blank=True,default=None)
    url=models.URLField(blank=True)



    def __unicode__(self):
        return self.title

class Imdb(models.Model):
    movieId=models.IntegerField(primary_key=True)
    imdb=models.CharField(max_length=20)
    tmdb=models.CharField(max_length=20)


class Rating(models.Model):
    userId= models.ForeignKey(User)
    movieId = models.IntegerField(default=None)
    title = models.CharField(max_length=1000, blank=True)
    genres = models.CharField(max_length=1000, blank=True)
    year = models.IntegerField(blank=True, default=None)
    url = models.URLField(blank=True)
    rating = models.DecimalField(decimal_places=6, max_digits=10)
    imdb=models.CharField(max_length=100,blank=True)



    def __unicode__(self):
        return self.title

