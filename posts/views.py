from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html')

def items(request):
    context = {
        'activeTab': 'items',
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