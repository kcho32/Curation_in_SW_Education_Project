from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'my_page'
urlpatterns = [
    path('', views.my_page, name='my_page'),
    path('update/', views.update, name='update'),
    path('my_lecture/', views.my_lecture, name='my_lecture'),
    path('delete/', views.delete, name='delete'),
    path('join_lecture/<int:id>', views.join_lecture, name='join_lecture'),
    path('cancel_lecture/<int:id>', views.cancel_lecture, name='cancel_lecture'),
    path('lecture_concern/<int:id>', views.lecture_concern, name='lecture_concern'),
    path('concerned_lecture/', views.concerned_lecture, name='concerned_lecture'),
    path('my_qna/', views.my_qna, name='my_qna'),

]