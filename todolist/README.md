## Link menuju Heroku :
## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CRSF sendiri merupakan kepanjangan dari Cross Site Request Forgery yang berguna untuk melindungi website dari serangan luar. CRSF sendiri merupakan bawaan dari django. Selain itu CRSF berguna untuk memastikan bahwa user yang melakukan login adalah user itu sendiri, maka dari itu CRSF memiliki token yang bersifat unik untuk setiap user
## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa, kita bisa dengan membuat sebuah tag. Tag tersebut harus memiliki atribut dan tipe yang sama dengan form pada django
## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika user mensubmit formnya, form tersebut akan mengirim "POST" request dan akan memanggil method dari views.py. Dari situ data akan divalidasi pada formulir django. Apabila data invalid, maka akan menampilkan bahwa ada kesalahan. Ketika data yang dimasukkan valid, maka request akan tersimpan di database, lalu akan ditampilkan di HTML dan server akan merespons dengan HTTP redirect ke url
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Buka terminal cmd yang ada pada vscode kemudian buat aplikasi baru dengan `python manage.py startapp todolist`
2. Pada `settings.py/project_django` tambahkan `'todolist'`, pada `INSTALLED_APPS`
3. Pada urls.py kita buat 
```
    from django.urls import path 
    from todolist.views import show_todolist,login_user,logout_user,register,create_task
    app_name = "todolist"
    urlpatterns = [
        path("",show_todolist,name="show_todolist"),
        path("login/",login_user,name="login_user"),
        path("logout/",logout_user,name="logout_user"),
        path("register/",register,name="register"),
        path("create-task/",create_task,name="create-task"),
        path("update/<int:pk>",update,name="update"),
        path("hapus/<int:pk>",hapus,name="hapus"),
    ]
```
4.  Pada models.py kita buat komponen yang kita butuhkan
```
    from django.db import models
    from django.contrib.auth.models import User

    class Task(models.Model):
        user = models.ForeignKey(User, on_delete = models.CASCADE)
        date = models.DateField()
        title = models.CharField(max_length = 255)
        description = models.TextField()
        is_finished = models.BooleanField()
``` 
5. Pada views.py buat fungsi-fungsi 
```
import datetime
from todolist.models import Task
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    todo = Task.objects.filter(user=user) 
    context = {
    'list': todo,
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
            date = datetime.timezone.now(),
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
```
6. Buat login.html, register.html, task.html, todolist.html pada folder templates
7. Kita routing pada todolist yang ada pada urls.py
8. Kita push dan deploy ke github, heroku
9. Buat dua akun user dan tiga dummy data