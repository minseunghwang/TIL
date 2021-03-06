from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('', views.index, name='index'),
]
