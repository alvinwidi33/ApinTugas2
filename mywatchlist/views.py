from django.shortcuts import render
from mywatchlist.models import MyWatchList
# Create your views here.
def show_my_watchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_mywatchlist' : data_mywatchlist,
        'nama' : 'Alvin Widi Nugroho',
        'npm' : '2106751902'
    }
    return render(request, "mywatchlist.html",context)