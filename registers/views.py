from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from posts.models import Item, User, DeliveredItem, Claimant
from django.db.models import Q

def isAuthenticated(request):
    token = request.session.get('user')
    if (token is None):
        return True
    return False

class RegistersView(ListView):
    template_name = 'registers.html'
    allow_empty = True
    queryset = Item.objects.all()
    ordering = ['-updated_at']
    paginate_by = 10

    STATUS_CHOICES = {
        'Lost': 'Perdido',
        'Delivered': 'Entregue',
        'Expired': 'Expirado'
    }
    
    def get_context_data(self, **kwargs):
        context = super(RegistersView, self).get_context_data(**kwargs)
        context_list = context['object_list']

        for item in context_list:
            item.created_at = item.created_at.strftime("%Y/%m/%d")
            item.updated_at = item.updated_at.strftime("%Y/%m/%d")
            item.when_was_found = item.when_was_found.strftime("%d/%m/%Y")
            item.withdrawal_deadline = item.withdrawal_deadline.strftime("%d/%m/%Y")
            item.shift = item.shift
            item.status = self.STATUS_CHOICES[item.status]
        
        context['object_list'] = context_list
        context.update({ 'activeTab': 'registers' })
        
        return context

class RegisterDetailsView(DetailView):
    template_name = 'details.html'
    allow_empty = True
    model = Item

    STATUS_CHOICES = {
        'Lost': 'Perdido',
        'Delivered': 'Entregue',
        'Expired': 'Expirado'
    }
    
    def get_context_data(self, **kwargs):
        context = super(RegisterDetailsView, self).get_context_data(**kwargs)
        context_object = context['object']
        if (context_object.status == 'Delivered'):
            context_object.withdrawal_data = DeliveredItem.objects.get(item=context_object.id)
            cpf = context_object.withdrawal_data.claimant.cpf
            cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
            context_object.withdrawal_data.claimant.cpf = cpf

        # context_object.created_at = context_object.created_at.strftime("%d/%m/%Y, %H:%M")
        context_object.when_was_found = context_object.when_was_found.strftime("%d/%m/%Y")
        context_object.withdrawal_deadline = context_object.withdrawal_deadline.strftime("%d/%m/%Y")
        context_object.shift = context_object.shift
        context_object.status = self.STATUS_CHOICES[context_object.status]
        
        context['object'] = context_object
        # context['object']['user'] = User.objects.get(registration=context_object.user_registration)
        context.update({ 'activeTab': 'registers' })
        
        return context

class RegistersSearchResultsView(ListView):
    template_name = 'registers.html'
    allow_empty = True
    ordering = ['-id']

    STATUS_CHOICES = {
        'Lost': 'Perdido',
        'Delivered': 'Entregue',
        'Expired': 'Expirado'
    }
    
    def get_context_data(self, **kwargs):
        context = super(RegistersSearchResultsView, self).get_context_data(**kwargs)
        context_list = context['object_list']

        for item in context_list:
            item.when_was_found = item.when_was_found.strftime("%d/%m/%Y")
            item.withdrawal_deadline = item.withdrawal_deadline.strftime("%d/%m/%Y")
            item.shift = item.shift
            item.status = self.STATUS_CHOICES[item.status]
        
        context['object_list'] = context_list
        context.update({ 'activeTab': 'registers','search': self.request.GET.get('keyword')  })
        
        return context

def searchRegister(request, text):
    print("TEXTO RECEBIDO -> ", text)
    registers = Item.objects.filter(name__icontains=text)

    STATUS_CHOICES = {
        'Lost': 'Perdido',
        'Delivered': 'Entregue',
        'Expired': 'Expirado'
    }

    for item in registers:
            item.created_at = item.created_at.strftime("%Y/%m/%d")
            item.updated_at = item.updated_at.strftime("%Y/%m/%d")
            item.when_was_found = item.when_was_found.strftime("%d/%m/%Y")
            item.withdrawal_deadline = item.withdrawal_deadline.strftime("%d/%m/%Y")
            item.shift = item.shift
            item.status = STATUS_CHOICES[item.status]
            
    print(registers)
    return render(request, 'item_register.html', { 'object_list': registers  })

