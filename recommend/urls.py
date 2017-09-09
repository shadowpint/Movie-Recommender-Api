"""recommend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

import engine.urls
import users.urls
from recommend import settings

urlpatterns = [
    # End points of social oauth.For more detail Go to the 'rest_framework_social_oauth2.urls' file
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    # Including all end points of admin panel.
    url(r'^admin/', include(admin.site.urls)),
    # Including all end points related to user. Go to 'users.urls' file
    url(r'^user/', include(users.urls)),
    # Including all end points related to aggregate records
    url(r'^recommend/', include(engine.urls)),
]
urlpatterns += [
    # End point to access uploaded live or environment files from browser
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_URL,
        }),
    ]