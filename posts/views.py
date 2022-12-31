from django.shortcuts import render, redirect
from .forms import ItemModelForm
from django.views.generic import CreateView, DeleteView
from .models import Item
from django.urls import reverse_lazy

def isAuthenticated(request):
    token = request.session.get('token')
    if (token is None):
        return True
    return False

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
                'status': 'Perdido',
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
                'status': 'Perdido',
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
                'id': 4,
                'status': 'Perdido',
                'image': 'image/jarra-de-vo.jpg',
                'name': 'Pipoqueira',
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
        'activeTab': 'delivered-items',
        'items': [
            {
                'id': 1,
                'status': 'Entregue',
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
                'id': 4,
                'status': 'Entregue',
                'image': 'image/jarra-de-vo.jpg',
                'name': 'Pipoqueira',
                'local_found': 'Na porta do refeitório',
                'when_was_found': '16/10/2022',
                'shift': 'noite',
                'withdrawal_deadline': '23/12/2022',
                'withdrawal_deadline': '23/12/2022',
                'pickup_location': 'Bloco principal',
            },
        ]
    }

    return render(request, 'delivered-items.html', context)

def expiredItems(request):
    context = {
        'activeTab': 'expired-items',
        'items': [
            {
                'id': 1,
                'status': 'Expirado',
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
            {
                'id': 4,
                'status': 'Expirado',
                'image': 'image/jarra-de-vo.jpg',
                'name': 'Pipoqueira',
                'local_found': 'Na porta do refeitório',
                'when_was_found': '16/10/2022',
                'shift': 'noite',
                'withdrawal_deadline': '23/12/2022',
                'withdrawal_deadline': '23/12/2022',
                'pickup_location': 'Bloco principal',
            },
        ]
    }

    return render(request, 'expired-items.html', context)


""" def create_post(request):
    if request.method == 'POST':
        form = ItemModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'create_post.html', {
                                                    'activeTab': 'items',
                                                    'form': form,})
    else:
        form = ItemModelForm()
        return render(request, 'create_post.html', {'activeTab': 'items','form': form})
 """

def complete_delivery(request):
    context = {
        'activeTab': 'items'
    }
    return redirect(reverse_lazy('login')) if isAuthenticated(request) else render(request, 'complete_delivery.html', context)


class ItemCreate(CreateView):
    model = Item
    form_class = ItemModelForm
    template_name = 'create_post.html'
    
    def get_context_data(self, **kwargs):
        context = super(ItemCreate, self).get_context_data(**kwargs)
        activeTab = 'items'
        context['activeTab'] = activeTab
        return context

    def get(self, request):
        if (isAuthenticated(request)):
            return redirect(reverse_lazy('login'))

        return render(request, 'create_post.html', { 'form': self.get_form(), 'activeTab': 'items' })
        
class ItemDelete(DeleteView):
    model = Item
    success_url = "items"
    queryset = 1
    template_name = "delete_post.html"

    def get(self, request):
        if (isAuthenticated(request)):
            return redirect(reverse_lazy('login'))
            
        return render(request, 'delete_post.html', { 'form': self.get_form(), 'activeTab': 'items' })

def tempDelete(request):
    context = {
        'activeTab': 'items'
    }

    return render(request, 'delete_post.html', context)