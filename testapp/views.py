from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from . import views

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Meghan is a Goddess" + " " + "Hail Seitan")
    
def prism(request):
    return render(request, 'prism.html')    
    
class Kitten(View):
    def get(self, request, *args, **kwargs):
        

        return render(
            request,
            '/kitten/kitten.html',
            context={
                
            }
        )   