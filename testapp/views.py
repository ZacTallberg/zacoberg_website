from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.conf import settings
from .models import KittenImage, FlowerImage
from .forms import KittenForm, KittenImageModelForm
import random
import os
import cv2
import glob


def getListOfKittens(): 
    list_of_kittens=[]
    for i in range(43):
        r=random.randint(1,43)
        if r not in list_of_kittens: list_of_kittens.append(r)
    
    return list_of_kittens

class HomePage(View):
    def get(self,request,*args,**kwargs):
        

        images = [cv2.imread(file) for file in glob.glob('static/images/kitten/*.jpg')]
        print(images)

        kitten = KittenImage.objects.create(file=images[5])
        all_kittens = KittenImage.objects.all()
        # for kitten in all_kittens:
        #     kitten.delete()
        # print(all_kittens)


        # kitten_form = KittenImageModelForm()
        kitten_form = KittenForm()

        return self.render(kitten_form=kitten_form, all_kittens=all_kittens)
    
    def post(self, request, *args, **kwargs):
        # kitten_form = KittenImageModelForm(request.POST)
        kitten_form = KittenForm(request.POST, request.FILES)

        if kitten_form.is_valid():
            kitten_form.save()
        else:
            self.render(kitten_form=kitten_form)
            print(kitten_form.errors)

        all_kittens = KittenImage.objects.all()
        print(vars(all_kittens))
        
        return self.render(kitten_form=kitten_form, all_kittens=all_kittens)

    def render (self, **kwargs):
        return render(self.request, 'homepage.html', context=kwargs)


class ReturnFiles(View):
    def get(self,request,*args,**kwargs):
        all_kittens = KittenImage.objects.all()

        
        r=random.randint(0,len(all_kittens)-1)

        print(len(all_kittens), r)


        kitten_url = all_kittens[r].file.url

        data = {'url': kitten_url}

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