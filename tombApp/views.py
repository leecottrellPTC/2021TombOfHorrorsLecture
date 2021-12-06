from django.http.response import HttpResponse
from django.shortcuts import render

class character:
    def __init__(self, name, hp, ac):
        self.charname = name
        self.hp = hp
        self.ac = ac

theChar = character("", "","")

# Create your views here.
def home_page(request):
    #html = "<html><body><h1>Welcome to the Tomb of Horrors</h1></html></body>"
    return render(request, 'home.html')

def lore_page(request):
    return render(request, 'lore.html')

def character_page(request):
    if request.method == 'POST':
        theChar = character(request.POST.get("charname"),
        request.POST.get("hitpoints"),
        request.POST.get("armor"))
        return render(request,'player.html', {'theChar' : theChar})

    else:
        return render(request, 'character.html' )
