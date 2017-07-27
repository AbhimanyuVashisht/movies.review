from __future__ import unicode_literals

from django.db import models
from movies.models import Movies


class Reviewers(models.Model):
    reviewer_id = models.CharField(max_length=100, primary_key=True, blank=False)
    email = models.EmailField('Reviewer Email', max_length=100, blank=False)

    class Meta:
        ordering = ('reviewer_id', )


class MovieReviews(models.Model):
    movie_id = models.CharField(max_length=100, primary_key=True, blank=False)
    fk_reviewer_id = models.ForeignKey(Reviewers)
    star_rate_movie = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0.00)
    review = models.TextField(max_length=100, blank=False)
    fk_id = models.ForeignKey(Movies)  # key to link Movies sudo key

    class Meta:
        ordering = ('movie_id', 'star_rate_movie', )
# Create your models here.
