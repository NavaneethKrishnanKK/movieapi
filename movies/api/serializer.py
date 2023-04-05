from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.Serializer):
    # id=serializers.IntegerField()
    name=serializers.CharField()
    year=serializers.IntegerField()
    director=serializers.CharField()
    genre=serializers.CharField()

class MovieModelSer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields="__all__"