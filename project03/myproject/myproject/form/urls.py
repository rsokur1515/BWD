from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.main_page, name='main'), 
    path('form/', views.form, name='form'),
    path('data/', views.data, name='data'),
    path('table/', views.table, name = 'table'),
    path('task_answer/', views.task_answer, name='task_answer'),
]