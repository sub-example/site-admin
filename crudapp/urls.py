from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'crudapp'

urlpatterns = [
    path('',views.signup, name='signup'),
    path('index',views.index,name='index'),
    path('info',views.info, name= 'info'),
    path('create',views.create, name='create'),
    path('update/<int:num>',views.update, name='update'),
    path('delete/<int:num>',views.delete,name='delete'),
    path('signup/',views.signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name="crudapp/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page="crudapp:login.html"),name='logout'),
    
]