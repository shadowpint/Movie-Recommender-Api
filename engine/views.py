import os

import django_filters
from django_filters import DateFilter
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from engine.compute import comp
from engine.tests import compi
from recommend.settings import MEDIA_ROOT
from .models import *
import json
from django.contrib.auth.models import User
from .serializers import *
import pandas as pd
from os import path

# sf = gl.SFrame({'userId': ['1', '1', '1', '1', '1', '1', '1', '1'],
#                 'movieId': ['2', '6', '7', '25', '46', '35', '48', '32'],
#                 'rating': [1.0, 2.5, 2.2, 2.2, 2.5, 2.3, 2.2, 2.8]})

import random


class ImdbList(APIView):
    """
    Get / Create questions
    """




    serializer_class = ImdbSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data=request.GET
        print data
        print data['movieId']
        queryset2=Imdb.objects.get(movieId=data['movieId'])
        serializer=ImdbSerializer(queryset2)
        return Response(serializer.data)

class MovieList(generics.ListCreateAPIView):
    """
    Get / Create questions
    """


    # queryset = Movie.objects.all().filter(movieId__in=random.sample(list(Movie.objects.all().values_list('movieId', flat=True)), 5))
    # queryset = Movie.objects.all()

    serializer_class = MovieSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = Movie.objects.all().filter(movieId__in=random.sample(list(Movie.objects.all().values_list('movieId', flat=True)), 5))
        serializer = MovieSerializer(queryset, many=True)
        ls=[]
        for i in queryset:
            print i.movieId
            print Imdb.objects.get(movieId=1664)
            ls.append(Imdb.objects.get(movieId=i.movieId).tmdb)
        queryset2=Imdb.objects.filter(tmdb__in=ls)
        serializer2=ImdbSerializer(queryset2,many=True)
        return Response(serializer.data)




class MovieDetail(generics.RetrieveDestroyAPIView):
    """
    Get / Delete questions
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]



class RatingList(APIView):
    """
    Get / Create questions
    """



    queryset = Rating.objects.all()


    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):


        print json.dumps(request.data)
        # print type(request.data)
        # movieid=json.dumps(request.data.keys())
        # movieid = eval(movieid)
        # rating=request.data.values()
        # print type(movieid)
        # print type(rating)

        userid=[str(9823)]
        print userid

        # print sf
        df2 = pd.DataFrame([[6041, 3578, 5], [6041, 2891, 4.5], [6041, 3050, 4.5],
                            [6041, 1218, 5], [6041, 3105, 3]],
                           columns=['UserID', 'MovieID', 'Rating'])
        # df=compi(df2)
        df=pd.read_csv(os.path.join(MEDIA_ROOT, 'result.csv'))
        js= df.to_json(orient='records')
        for index, row in df.iterrows():
            rating = Rating.objects.create(userId=request.user,movieId=row['movieId'],title=row['title'],genres=row['genres'],year=row['year'],url=row['url'],rating=row['rating'],imdb=Imdb.objects.get(movieId=row['movieId']).tmdb)
            rating.save()
        ratings = Rating.objects.filter(userId=request.user.pk)
        serializer = RatingSerializer(ratings, many=True)


        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        id = request.user.pk
        ratings = Rating.objects.filter(userId=id)

        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)


class RatingDetail(generics.RetrieveUpdateAPIView):
    """
    Get / Update a Choice
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
# class Calculate(APIView):
#     permission_classes = [AllowAny]
#     def get(self, request, format=None):
#         df2 = pd.read_csv(os.path.join(MEDIA_ROOT, 'movie_data.csv'))
#         for index, row in df2.iterrows():
#             idb = Imdb.objects.create(movieId=row['movieId'], imdb=row['imdbId'], tmdb=row['tmdbId'])
#             # print row['imdbId']
#             idb.save()



