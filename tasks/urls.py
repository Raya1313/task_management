from django.urls import path
from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.menu, name='home'),
    path('<int:id>/', views.task_details, name='task_details'),
    path('<int:id>/status/', views.set_status, name='set_status'),
    path('filter/<int:status>/', views.filter_tasks, name='filter_tasks')
]
