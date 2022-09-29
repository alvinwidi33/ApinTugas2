from django.urls import path 
from todolist.views import show_todolist,login_user,logout_user,register,create_task, update,hapus
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
