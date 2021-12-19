from django.http.response import HttpResponse
from django.shortcuts import render
from tombApp.models import character

# class character:
#     def __init__(self, name, hp, ac):
#         self.charname = name
#         self.hp = hp
#         self.ac = ac

theChar = None

# Create your views here.
def home_page(request):
    global theChar
    #html = "<html><body><h1>Welcome to the Tomb of Horrors</h1></html></body>"
    return render(request, 'home.html', {'theChar' : theChar})

def lore_page(request):
    global theChar
    return render(request, 'lore.html', {'theChar' : theChar})

def character_page(request):
    global theChar
    if request.method == 'POST':
        theChar = character('',request.POST.get("charname"),
        request.POST.get("hitpoints"),
        request.POST.get("armor"))
        #request.session.
        return render(request,'player.html', {'theChar' : theChar})

    else:
        return render(request, 'character.html', {'theChar' : theChar} )
