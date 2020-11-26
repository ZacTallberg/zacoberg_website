
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('prism/', views.prism, name='prism'),
    path('kitten/', views.Kitten.as_view(), name='kitten'),
    url(r'^ajax/load_image/$', views.ReturnFiles.as_view(), name='load-image'),
    # path('load_image/', views.ReturnFiles.as_view(), name='load-image'),
]


