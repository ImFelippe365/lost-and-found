from django.shortcuts import render

# Create your views here.

def create_post(request):
    context = {

    }

    return render(request, 'create_post.html', context)