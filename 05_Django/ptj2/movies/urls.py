from django.urls import path
from . import views

app_name='movies'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:movies_pk>/detail/', views.detail, name='detail'),
    path('', views.index, name='index'),
]
