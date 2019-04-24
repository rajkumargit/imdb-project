"""
Serializers.py
"""
from rest_framework import serializers
from .models import Movie


class MovieListSerializer(serializers.ModelSerializer):
    """
    Serializer for movie list
    """
    class Meta:
        """
        Meta Data
        """
        fields = ('title', 'genre', 'year', 'rating', 'run_time_minutes', 'description')
        model = Movie


class MovieSerializer(serializers.Serializer):
    """
    Serializer for movie
    """
    rank = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    genre = serializers.CharField(max_length=100)
    description = serializers.CharField()
    director = serializers.CharField(max_length=200)
    actors = serializers.CharField(max_length=500)
    year = serializers.IntegerField()
    run_time_minutes = serializers.IntegerField()
    rating = serializers.CharField(max_length=10)
    votes = serializers.CharField(max_length=10)
    revenue_millions = serializers.CharField(max_length=10)
    meta_score = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Movie.objects.update(**validated_data)

    class Meta:
        """
        Meta Data
        """
        fields = serializers.ALL_FIELDS
        model = Movie
