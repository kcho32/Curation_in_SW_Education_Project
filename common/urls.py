from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'common'

urlpatterns = [
    #path('', views.main, name='main'),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('find_id/', views.find_id, name='find_id'),
    path('find_pw/', views.find_pw, name='find_pw'),
    path('find_pw/reset_pw/<int:pk>', views.reset_pw, name='reset_pw'),
    path('find_pw/verify/<int:pk>', views.verify, name='verify'),
    path('lecture/searching/', views.searched_lecture, name='searched_lecture'),
    path('message/', views.customer_message, name='customer_message'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
