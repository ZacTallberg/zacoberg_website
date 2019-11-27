
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prism/', views.prism, name='prism'),
    path('kitten/', views.Kitten.as_view(), name='kitten'),
]


