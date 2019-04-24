"""
utils.py
"""
from .models import Movie


class MovieTestData:
    """
    Movie Test Data
    """
    @staticmethod
    def generate_data():
        """
        Create Movies for testing
        :return:
        """
        Movie.objects.create(
            rank=1,
            title='Guardians of the Galaxy',
            genre='Action,Adventure,Sci-Fi',
            description='A group of intergalactic criminals are forced to work together to stop a '
                        'fanatical warrior from taking control of the universe.',
            director='James Gunn',
            actors='Chris Pratt, Vin Diesel, Bradley Cooper, Zoe Saldana',
            year=2014,
            run_time_minutes=121,
            rating='8.1',
            votes='757074',
            revenue_millions='333.13',
            meta_score='76'
        )
        Movie.objects.create(
            rank=2,
            title='Split',
            genre='Horror,Thriller',
            description='Three girls are kidnapped by a man with a diagnosed 23 distinct '
                        'personalities. They must try to escape before the apparent '
                        'emergence of a frightful new 24th.',
            director='M. Night Shyamalan',
            actors='James McAvoy, Anya Taylor-Joy, Haley Lu Richardson, Jessica Sula',
            year=2016,
            run_time_minutes=131,
            rating='4.1',
            votes='7074',
            revenue_millions='133.13',
            meta_score='96'
        )
        Movie.objects.create(
            rank=3,
            title='La La Land',
            genre='Comedy,Drama,Music',
            description='A jazz pianist falls for an aspiring actress in Los Angeles.',
            director='Damien Chazelle',
            actors='Ryan Gosling, Emma Stone, Rosemarie DeWitt, J.K. Simmons',
            year=2015,
            run_time_minutes=121,
            rating='7.1',
            votes='77074',
            revenue_millions='93.13',
            meta_score='86'
        )
