from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
def show_my_watchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_mywatchlist' : data_mywatchlist,
        'nama' : 'Alvin Widi Nugroho',
        'npm' : '2106751902'
    }
    return render(request, "mywatchlist.html",context)

def show_xml(request):
    data =  MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data =  MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")