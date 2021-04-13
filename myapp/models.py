from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=20)
    dor = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Cast(models.Model):
    name = models.CharField(max_length=29)
    age = models.PositiveIntegerField()
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

# Create your models here.
