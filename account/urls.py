from django.urls import path
from . import views

urlpatterns = [

    path('search/', views.search_student, name="search-student"),
    path('login/', views.user_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path('register/', views.getRegister, name="register"),
    #path('topics', views.getCategory, name="category"),
    #path('create/topic', views.createTopic, name="createTopic"),



    #account confirmations
     #path('activate/<uid>/<token>/', views.activate, name='activate'),
    #path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
]