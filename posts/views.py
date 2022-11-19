from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html')

def items(request):
    context = {
        'activeTab': 'items'
    }

    return render(request, 'items.html', context)

def deliveredItems(request):
    context = {
        'activeTab': 'delivered-items'
    }

    return render(request, 'delivered-items.html', context)

def expiredItems(request):
    context = {
        'activeTab': 'expired-items'
    }

    return render(request, 'expired-items.html', context)

def allRegisters(request):
    context = {
        'activeTab': 'all-registers'
    }

    return render(request, 'all-registers.html', context)
