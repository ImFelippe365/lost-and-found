from django.shortcuts import render, redirect
from .forms import ItemModelForm, CompleteDeliveryModelForm
from django.views.generic import CreateView, DeleteView, ListView
from .models import Item, DeliveredItem
from django.urls import reverse_lazy

def isAuthenticated(request):
    token = request.session.get('token')
    if (token is None):
        return True
    return False

class ItemView(ListView):
    template_name = 'items.html'
    queryset = Item.objects.all()

    item = Item.objects.get(id=1)
    print(item.when_was_found.day, item.when_was_found.month, item.when_was_found.year)

    SHIFT_CHOICES = {
        'Morning': 'Manhã',
        'Afternoon': 'Tarde',
        'Night': 'Noite'
    }
    
    STATUS_CHOICES = {
        'Lost': 'Perdido',
        'Delivered': 'Entregue',
        'Expired': 'Expirado'
    }
    
    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context_list = context['object_list']
        
        for item in context_list:
            when_was_found = f'{item.when_was_found.day}/{item.when_was_found.month}/{item.when_was_found.year}'
            item.when_was_found = when_was_found
            item.withdrawal_deadline = f'{item.withdrawal_deadline.day}/{item.withdrawal_deadline.month}/{item.withdrawal_deadline.year}'
            item.shift = self.SHIFT_CHOICES[item.shift if item.shift else 'Morning']
            item.status = self.STATUS_CHOICES[item.status if item.status else 'Lost']
        
        # context = RequestContext(self.request, {
        #     'object_list': context
        # })
        context['object_list'] = context_list
        context.update({'activeTab': 'items'})
        
        return context


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

""" def complete_delivery(request):
    context = {
        'activeTab': 'items'
    }
    return redirect(reverse_lazy('login')) if isAuthenticated(request) else render(request, 'complete_delivery.html', context) """


class ItemCreate(CreateView):
    model = Item
    form_class = ItemModelForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('items')

    def get(self, request):
        if (isAuthenticated(request)):
            return redirect(reverse_lazy('login'))

        return render(request, 'create_post.html', { 'form': self.get_form(), 'activeTab': 'items' })

    def form_valid(self, form):
        user = self.request.session.get('user')
        form.instance.user_registration = user['registration']
        return super(ItemCreate, self).form_valid(form)
        
        
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


class CompleteDelivery(CreateView):
    model = DeliveredItem
    form_class = CompleteDeliveryModelForm
    template_name = 'complete_delivery.html'
    success_url = reverse_lazy('complete-delivery')

    def get(self, request):
        if (isAuthenticated(request)):
            return redirect(reverse_lazy('login'))

        return render(request, 'complete_delivery.html', { 'form': self.get_form(), 'activeTab': 'items' })