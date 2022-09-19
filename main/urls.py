from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('send', views.send, name='send'),
    path('confirm/<int:personID>', views.confirm, name='confirm'),
    path('confirm/<int:personID>/<str:hash>', views.confirm, name='confirm'),
    path('success', views.success, name='success'),
]