from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    #html = "<html><body><h1>Welcome to the Tomb of Horrors</h1></html></body>"
    return render(request, 'home.html')

def lore_page(request):
    return render(request, 'lore.html')
