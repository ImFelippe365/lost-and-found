from django.shortcuts import render

# Create your views here.

def create_post(request):
    context = {
        'activeTab': 'items'
    }

    return render(request, 'create_post.html', context)

def complete_delivery(request):
    context = {
        'activeTab': 'items'
    }
    return render(request, 'complete_delivery.html', context)