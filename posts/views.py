from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html')

def itens(request):

    return render(request, 'itens.html')