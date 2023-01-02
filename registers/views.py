from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

def isAuthenticated(request):
    token = request.session.get('token')
    if (token is None):
        return True
    return False

def allRegisters(request):
    context = {
        'activeTab': 'all-registers',
        'items': [
            {
                'id': 1,
                'status': 'Expirado',
                'image': 'image/jarra-de-vo.jpg',
                'name': 'Jarra de porcelana',
                'who_found': 'José Manoel',
                'local_found': 'Sala 61',
                'when_was_found': '16/10/2022',
                'shift': 'noite',
                'withdrawal_deadline': '23/12/2022',
                'withdrawal_deadline': '23/12/2022',
                'pickup_location': 'Bloco principal',
            },
            {
                'id': 2,
                'status': 'Expirado',
                'image': 'image/jarra-de-vo.jpg',
                'name': 'Jarra de porcelana',
                'who_found': 'José Manoel',
                'local_found': 'Na porta do refeitório',
                'when_was_found': '16/10/2022',
                'shift': 'noite',
                'withdrawal_deadline': '23/12/2022',
                'withdrawal_deadline': '23/12/2022',
                'pickup_location': 'Bloco principal',
            },
            {
                'id': 3,
                'status': 'Expirado',
                'image': 'image/jarra-de-vo.jpg',
                'name': 'Jarra de porcelana',
                'who_found': 'José Manoel',
                'local_found': 'Na porta do refeitório',
                'when_was_found': '16/10/2022',
                'shift': 'noite',
                'withdrawal_deadline': '23/12/2022',
                'withdrawal_deadline': '23/12/2022',
                'pickup_location': 'Bloco principal',
            },
            {
                'id': 4,
                'status': 'Expirado',
                'image': 'image/jarra-de-vo.jpg',
                'name': 'Pipoqueira',
                'who_found': 'José Manoel',
                'local_found': 'Na porta do refeitório',
                'when_was_found': '16/10/2022',
                'shift': 'noite',
                'withdrawal_deadline': '23/12/2022',
                'withdrawal_deadline': '23/12/2022',
                'pickup_location': 'Bloco principal',
            },
        ]
    }

    return redirect(reverse_lazy('login')) if isAuthenticated(request) else render(request, 'all-registers.html', context)

class Registers(ListView):
    pass

def details(request):
    context = {
        'activeTab': 'all-registers',
        'items': [
            {
                'id': 1,
                'status': 'Perdido',
                'image': 'image/jarra-de-vo.jpg',
                'name': 'Jarra de porcelana',
                'local_found': 'Sala 61',
                'when_was_found': '16/10/2022',
                'shift': 'noite',
                'withdrawal_deadline': '23/12/2022',
                'withdrawal_deadline': '23/12/2022',
                'pickup_location': 'Bloco principal',
            },
            {
                'id': 2,
                'status': 'Entregue',
                'image': 'image/jarra-de-vo.jpg',
                'name': 'Jarra de porcelana',
                'local_found': 'Na porta do refeitório',
                'when_was_found': '16/10/2022',
                'shift': 'noite',
                'withdrawal_deadline': '23/12/2022',
                'withdrawal_deadline': '23/12/2022',
                'pickup_location': 'Bloco principal',
            },
            {
                'id': 3,
                'status': 'Expirado',
                'image': 'image/jarra-de-vo.jpg',
                'name': 'Jarra de porcelana',
                'local_found': 'Na porta do refeitório',
                'when_was_found': '16/10/2022',
                'shift': 'noite',
                'withdrawal_deadline': '23/12/2022',
                'withdrawal_deadline': '23/12/2022',
                'pickup_location': 'Bloco principal',
            },
        ]
    }

    return redirect(reverse_lazy('login')) if isAuthenticated(request) else render(request, 'details.html', context)
