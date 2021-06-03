from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def calpage(request):
    return render(request, 'calpage.html')


def cal(request):
    va = request.POST['valueA']
    vb = request.POST['valueB']
    result = int(va) + int(vb)
    return render(request, 'result.html', context={'data': result})
