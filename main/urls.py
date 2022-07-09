from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name = 'home'),
    # path('google_oauth/redirect/', RedirectOauthView),
    path('google_oauth/callback/', CallbackView)
]

