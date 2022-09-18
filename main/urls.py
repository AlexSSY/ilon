from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('send', views.send, name='send'),
    path('success', views.success, name='success'),
]