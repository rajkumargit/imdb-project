"""
views.py
"""
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_csv.parsers import CSVParser
from .models import Movie
from .serializers import MovieListSerializer, MovieSerializer


class BulkMovieCreateView(generics.ListCreateAPIView):
    """
    Create Movies in Bulk
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    parser_classes = (CSVParser,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        cleaned_data = [d for d in request.data if any(d.values())]
        count = 0
        for movie in cleaned_data:
            try:
                Movie.objects.get(title=movie['Title'])
            except Movie.DoesNotExist:
                Movie.objects.create(
                    rank=movie['Rank'],
                    title=movie['Title'],
                    genre=movie['Genre'],
                    description=movie['Description'],
                    director=movie['Director'],
                    actors=movie['Actors'],
                    year=movie['Year'],
                    run_time_minutes=movie['Runtime (Minutes)'],
                    rating=movie['Rating'],
                    votes=movie['Votes'],
                    revenue_millions=movie['Revenue (Millions)'],
                    meta_score=movie['Metascore']
                )
                count = count + 1
        return Response(count, status=status.HTTP_201_CREATED, headers={})


class MovieListByYearView(generics.ListAPIView):
    """
    Get Movies by year or year range(Defaults to 2016)
    """
    serializer_class = MovieListSerializer

    def get_queryset(self):
        """
        Override queryset to apply filters

        :return: filtered queryset
        """
        start_year = self.kwargs.get('start_year')
        end_year = self.kwargs.get('end_year')
        if not start_year:
            start_year = 2016
        if not end_year:
            end_year = start_year
        movie_list = Movie.objects.filter(year__range=[start_year, end_year]).order_by('-rating')
        return movie_list


class MovieListByGenreView(generics.ListAPIView):
    """
    Get Movies by Genre. Defaults to no genre
    """
    serializer_class = MovieListSerializer

    def get_queryset(self):
        """
        Override queryset to apply filters

        :return: filtered queryset
        """
        genre = self.kwargs.get('genre')
        if genre:
            movie_list = Movie.objects.filter(genre__contains=genre).order_by('-rating')
        else:
            movie_list = Movie.objects.all().order_by('-rating')
        return movie_list
