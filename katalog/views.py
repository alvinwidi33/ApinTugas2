from django.shortcuts import render
from katalog.models import CatalogItem
from django.http import HttpResponse
from django.core import serializers

def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_barang' : data_katalog,
        'nama' : 'Alvin Widi Nugroho',
        'npm' : '2106751902'
    }
    return render(request, 'katalog.html', context)



