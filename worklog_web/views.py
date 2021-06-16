from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, 'login2.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def signpage(request):
    return render(request, 'signpage.html')


