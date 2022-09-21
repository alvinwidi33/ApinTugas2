from django.urls import path
from mywatchlist.views import show_my_watchlist

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_my_watchlist, name='show_my_watchlist'),
]