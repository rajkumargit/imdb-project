"""
models.py
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Movie(models.Model):
    """
    Movie model
    """
    rank = models.SmallIntegerField()
    title = models.CharField(max_length=100, unique=True)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=200)
    actors = models.CharField(max_length=500)
    year = models.SmallIntegerField()
    run_time_minutes = models.SmallIntegerField()
    rating = models.CharField(max_length=10)
    votes = models.CharField(max_length=10)
    revenue_millions = models.CharField(max_length=10)
    meta_score = models.CharField(max_length=10)
