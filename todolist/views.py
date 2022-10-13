import datetime
from todolist.models import Task
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    # todo = Task.objects.filter(user=user) 
    context = {
    #'list': todo,
    'nama': user,
    'last_login': request.COOKIES,  
}
    return render(request,"todolist.html",context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":

        Task.objects.create(
            user = request.user,
            title = request.POST.get("title"),
            description = request.POST.get("description"),
            date = datetime.datetime.today(),
            is_finished = False
        )
        
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    return render(request, "task.html")

@login_required(login_url='/todolist/login/')
def update(request,pk):
    task = Task.objects.filter(user=request.user).get(pk=pk)
    if (task.is_finished) :
        task.is_finished = False
    else :
        task.is_finished = True
    task.save()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))
    
@login_required(login_url='/todolist/login/')
def hapus(request,pk):
    task = Task.objects.filter(user=request.user).get(pk=pk)
    task.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", task), content_type="application/json")

def add_todolist(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_barang = Task.objects.create(user=request.user, is_finished=False, title = title, description=description,date=datetime.datetime.now())
        new_barang.save()
        return HttpResponse(b"CREATED")

    return HttpResponseNotFound()
        # hasil = {
        #     'fields':{
        #         'title':new_barang.title,
        #         'description':new_barang.description,
        #         'date':new_barang.date,
        #     },
        #     'pk':new_barang.pk
        # }
        # return JsonResponse(hasil)