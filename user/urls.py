from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('addpost/', views.user_addpost, name='addpost'),
    path('logout/', views.user_logout, name='logout'),
]
