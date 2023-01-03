from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from posts.models import Item

def isAuthenticated(request):
    token = request.session.get('token')
    if (token is None):
        return True
    return False

class Registers(ListView):
    template_name = 'registers.html'
    allow_empty = True
    queryset = Item.objects.all()

    STATUS_CHOICES = {
        'Lost': 'Perdido',
        'Delivered': 'Entregue',
        'Expired': 'Expirado'
    }
    
    def get_context_data(self, **kwargs):
        context = super(Registers, self).get_context_data(**kwargs)
        context_list = context['object_list']

        for item in context_list:
            item.when_was_found = item.when_was_found.strftime("%m/%d/%Y")
            item.withdrawal_deadline = item.withdrawal_deadline.strftime("%m/%d/%Y")
            item.shift = item.shift
            item.status = self.STATUS_CHOICES[item.status]
        
        context['object_list'] = context_list
        context.update({ 'activeTab': 'registers' })
        
        return context

class RegisterDetails(DetailView):
    template_name = 'details.html'
    allow_empty = True
    model = Item

    STATUS_CHOICES = {
        'Lost': 'Perdido',
        'Delivered': 'Entregue',
        'Expired': 'Expirado'
    }
    
    def get_context_data(self, **kwargs):
        context = super(RegisterDetails, self).get_context_data(**kwargs)
        context_object = context['object']

        context_object.when_was_found = context_object.when_was_found.strftime("%m/%d/%Y")
        context_object.withdrawal_deadline = context_object.withdrawal_deadline.strftime("%m/%d/%Y")
        context_object.shift = context_object.shift
        context_object.status = self.STATUS_CHOICES[context_object.status]
        
        context['object'] = context_object
        context.update({ 'activeTab': 'registers' })
        
        return context

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
