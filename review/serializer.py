from rest_framework import serializers
from models import *
from django.contrib.auth import get_user_model

user = get_user_model()


class ReviewersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewers
        fields = ('reviewer_id', 'email')


class MovieReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReviews
        fields = ('movie_id', 'fk_reviewer_id', 'star_rate_movie', 'review', 'fk_id')
