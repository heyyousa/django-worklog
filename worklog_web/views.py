from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, 'login.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def cal(request):
    va = request.POST['valueA']
    vb = request.POST['valueB']
    result = int(va) + int(vb)
    return render(request, 'result.html', context={'data': result})
