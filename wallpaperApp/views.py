# meu_app/views.py
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


from .models import Group
context = {
    'links':{
        "asdadasdada",
        'asdasdasdas',
        'asdasdasaasd'
    }
}

def home(request):
    return render(request, 'wallpaperApp/home.html', context)
