from rest_framework import serializers


from .models import *

# class FooSerializer(serializers.ModelSerializer):
#   my_field = serializers.SerializerMethodField('is_named_bar')
#
#   def is_named_bar(self, foo):
#       return foo.name == "bar"
#
#   class Meta:
#     model = Movie
#     fields = ('movieId', 'title', 'genres','year','url','my_field')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ImdbSerializer(serializers.ModelSerializer):
            class Meta:
                model = Imdb
                fields = ['movieId','tmdb']
class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'




