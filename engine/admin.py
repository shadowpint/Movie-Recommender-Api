from django.contrib import admin

# Register your models here.


# Register your models here.
from .models import *
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movieId','year')
    # list_filter = [ 'year']
    search_fields = ['movieId']
admin.site.register(Rating)
class ImdbAdmin(admin.ModelAdmin):
    list_display = ('movieId','imdb')
    search_fields = ['movieId']
admin.site.register(Movie,MovieAdmin)
admin.site.register(Imdb,ImdbAdmin)