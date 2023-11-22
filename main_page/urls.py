from django.urls import path
from .views import string_post_view, game_detail_view

urlpatterns = [
    path('home_page/', string_post_view),
    path('game_detail/<int:id>/', game_detail_view),
]