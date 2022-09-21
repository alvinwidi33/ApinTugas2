from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
def show_my_watchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    watched = 0
    have_not_watched = 0
    msg = ""
    for i in data_mywatchlist:
        if i.watched == "Yes":
            watched+=1
        else:
            have_not_watched+=1
    if watched >= have_not_watched:
        msg = "Selamat, kamu sudah banyak menonton!"
    else:
        msg = "Wah, kamu masih sedikit menonton!"
    context = {
        'list_mywatchlist' : data_mywatchlist,
        'nama' : 'Alvin Widi Nugroho',
        'npm' : '2106751902',
        'pesan': msg
    }
    return render(request, "mywatchlist.html",context)

def show_xml(request):
    data =  MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data =  MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")