from django.shortcuts import render
import subprocess

# Create your views here.

def index(request):
    return render(request, 'mainSite/index.html')