from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext
#from django.shortcuts import render_to_response
from django.conf.urls.static import static
#from django.contrib.staticfiles.templatetags import static
from django.contrib.staticfiles.storage import staticfiles_storage
from . import views
import random
import os 
import cv2 
import glob 
import base64 

# Create your views here.
def index(request):

    rand_int = random.randrange(0, 20, True)

    return render(
        request, 
        'index.html', 
        context={
        'rand_int':rand_int,
        }
    )
    
def prism(request):
    return render(request, 'prism.html')    
    
class Kitten(View):
    def get(self, request, *args, **kwargs):
        url = static('images/')
        all_images = load_all_images(url)
        print(all_images)
        return render(
            request,
            '/kitten/kitten.html',
            context={
                'all_images':all_images,
            }
        )   

def load_all_images():
    
    #images = [cv2.imread(file) for file in glob.glob('{{url}}*.jpg')]         
    return url_path         