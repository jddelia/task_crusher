from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='users-profile'),
    path('createtask/', views.create_task, name='users-createtask'),
    path('delete', views.delete_task, name='users-deletetask')
]
