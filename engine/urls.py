from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    # Regular Django Views


    # API views
    url(r'^api/rating/$', views.RatingList.as_view()),
    url(r'^api/movie/$', views.MovieList.as_view()),
url(r'^api/imdb/$', views.ImdbList.as_view()),
# url(r'^api/calculate/$', views.Calculate.as_view()),
    url(r'^api/movie/(?P<pk>[0-9]+)/$', views.MovieDetail.as_view()),

    url(r'^api/rating/(?P<pk>[0-9]+)/$', views.RatingDetail.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
