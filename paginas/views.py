from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'paginas/index.html')


def blog(request):
    return render(request, 'paginas/blog.html')


def sobre(request):
    return render(request, 'paginas/sobre.html')
