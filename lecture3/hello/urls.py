from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>/', views.greating, name='greating'),
    path('dipu/', views.dipu, name='dipu'),
    path('ramiza/', views.ramiza, name='ramiza'),
]
