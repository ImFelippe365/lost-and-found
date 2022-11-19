from django.shortcuts import render

# Create your views here.

def allRegisters(request):
    context = {
        'activeTab': 'all-registers'
    }

    return render(request, 'all-registers.html', context)

def details(request):
    context = { }

    return render(request, 'details.html', context)
