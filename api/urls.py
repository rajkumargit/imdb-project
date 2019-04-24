"""
urls.py
"""
from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.BulkMovieCreateView.as_view()),
    path('movies/year/', views.MovieListByYearView.as_view()),
    path('movies/year/<start_year>/', views.MovieListByYearView.as_view()),
    path('movies/year/<start_year>/<end_year>/', views.MovieListByYearView.as_view()),
    path('movies/genre/', views.MovieListByGenreView.as_view()),
    path('movies/genre/<genre>/', views.MovieListByGenreView.as_view())
]
