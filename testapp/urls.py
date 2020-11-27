
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('prism/', views.prism, name='prism'),
    path('kitten/', views.Kitten.as_view(), name='kitten'),
    url(r'^ajax/load_image/$', views.ReturnFiles.as_view(), name='load-image'),
    # path('load_image/', views.ReturnFiles.as_view(), name='load-image'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
