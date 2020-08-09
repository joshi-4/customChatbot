from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import mimetypes
import os

# Create your views here.
@login_required
def index(request):
    return render(request, 'mainSite/index.html')

def about(request):
    return render(request, 'mainsite/about.html')

def register(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'mainsite/register.html', context)

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'] )
        if user is not None:
            auth.login(request, user)
            return redirect('index')
    return render(request,'mainsite/login.html')

@login_required
def logout(request):
	auth.logout(request)
	return redirect('login')

@login_required
def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.content_type)
        if uploaded_file.content_type == 'text/plain':
            content = uploaded_file.read().decode("utf-8")
            print(content)
        elif uploaded_file.content_type == 'application/pdf':
            print("Pdf")
        else:
            print("Document Type Not Supported")
        
    
    return render(request, 'mainsite/index.html')


def download_apk(request):
    filepath = 'mainSite/chatbot/bin/temp.txt'
    filename = "temp.txt"
    #filename = "temp.txt"
    fl = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(fl, content_type = mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response