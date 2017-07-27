from rest_framework import serializers
from models import *
from django.contrib.auth import get_user_model
import json

User = get_user_model()


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('uuid', 'title', 'description', 'release_date', 'director', 'cast', 'star_rate', 'generic_type')
