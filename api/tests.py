"""
tests.py
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .utils import MovieTestData
from .views import MovieListByYearView, MovieListByGenreView


class MovieTest(TestCase):
    """
    Movie Test
    """
    def setUp(self):
        """
        Test SetUp
        :return:
        """
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()
        MovieTestData.generate_data()

    def test_movie_list_by_genre(self):
        """
        Test method for movie list by genre

        :return:
        """
        kwargs = {'genre': 'action'}
        request = self.factory.get('/api/movies/genre')
        response = MovieListByGenreView.as_view()(request, **kwargs)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['genre'], 'Action,Adventure,Sci-Fi')

    def test_movie_list_by_year(self):
        """
        Test method for movie list by year

        :return:
        """
        kwargs = {'start_year': '2014'}
        request = self.factory.get('/api/movies/year')
        response = MovieListByYearView.as_view()(request, **kwargs)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

    def test_movie_list_by_year_range(self):
        """
        Test method for movie list by year range

        :return:
        """
        kwargs = {'start_year': '2012', 'end_year': '2015'}
        request = self.factory.get('/api/movies/year')
        response = MovieListByYearView.as_view()(request, **kwargs)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
