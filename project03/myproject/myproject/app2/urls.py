from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.first_page, name='main'),
    path('page/<int:pk>', views.page, name='page'),
]