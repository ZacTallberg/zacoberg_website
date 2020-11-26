from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.conf import settings
import random
import os


def getListOfKittens(): 
    list_of_kittens=[]
    for i in range(43):
        r=random.randint(1,43)
        if r not in list_of_kittens: list_of_kittens.append(r)
    
    return list_of_kittens

class HomePage(View):
    def get(self,request,*args,**kwargs):

        
        print(settings.STATIC_ROOT)
        print(settings.STATICFILES_DIRS)

        return render(
        request, 
        'homepage.html', 
        context={
        }
    )

class ReturnFiles(View):
    def get(self,request,*args,**kwargs):
        
        path = '/static/images/kitten/'
        all_files = os.listdir(path)
        r=random.randint(1,43)
        image_path = path + all_files[r]
        path_test = image_path
        print(path_test)
        data = {'url': path_test}

        return JsonResponse(data)
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