from django.db import models

# Create your models here.

movies=[
    {"id":1,"name":"Spadikam","year":1996,"director":"Bhadran","genre":"drama"},
    {"id":2,"name":"Premam","year":2015,"director":"Alphons Puthrein","genre":"romance"},
    {"id":3,"name":"Arya","year":2004,"director":"Sukumar","genre":"romance"},
    {"id":4,"name":"Lucifer","year":2019,"director":"Prithwiraj","genre":"thriller"},
    {"id":5,"name":"DSMM","year":2022,"director":"Sam Raini","genre":"fantacy"},
]

class Movies(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField()
    director=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)