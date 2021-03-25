from django.urls import path
from . import views

urlpatterns = [

    path('dashboard',views.Dashboard, name='dashboard'),
    path('signup', views.Create_User, name= 'create_user'),
    path('login', views.user_login, name= 'login'),
    path('logout', views.user_logout, name='logout')

    
    
    
]
