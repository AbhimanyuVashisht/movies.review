# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.db import models


class Movies(models.Model):
    generic_type_choice = (
        ('MV', 'Movies'),
        ('TV', 'TVShows'),
    )
    uuid = models.CharField(max_length=100, primary_key=True, blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200, blank=True, default='')
    release_date = models.DateField()
    director = models.CharField(max_length=100, blank=False)
    cast = models.CharField(max_length=100, blank=True)
    star_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0.00)
    generic_type = models.CharField(max_length=2, choices=generic_type_choice, default='MV')
    # owner = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    class Meta:
            ordering = ('star_rate', 'uuid', )

    # Create your models here.
