from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemModelForm, CompleteDeliveryModelForm
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Item, DeliveredItem
from django.urls import reverse_lazy
from django.db import transaction

def isAuthenticated(request):
    token = request.session.get('token')
    if (token is None):
        return True
    return False


class ItemsView(ListView):
    template_name = 'items.html'
    allow_empty = True
    queryset = Item.objects.all().filter(status='Lost')

    STATUS_CHOICES = {
        'Lost': 'Perdido',
        'Delivered': 'Entregue',
        'Expired': 'Expirado'
    }

    def get_context_data(self, **kwargs):
        context = super(ItemsView, self).get_context_data(**kwargs)
        context_list = context['object_list']

        for item in context_list:
            item.when_was_found = item.when_was_found.strftime("%d/%m/%Y")
            item.withdrawal_deadline = item.withdrawal_deadline.strftime(
                "%d/%m/%Y")
            item.shift = item.shift
            item.status = self.STATUS_CHOICES[item.status]

        context['object_list'] = context_list
        context.update({'activeTab': 'items'})

        return context


class DeliveredItemsView(ListView):
    template_name = 'delivered_items.html'
    allow_empty = True
    queryset = Item.objects.all().filter(status='Delivered')

    STATUS_CHOICES = {
        'Lost': 'Perdido',
        'Delivered': 'Entregue',
        'Expired': 'Expirado'
    }

    def get_context_data(self, **kwargs):
        context = super(DeliveredItemsView, self).get_context_data(**kwargs)
        context_list = context['object_list']

        for item in context_list:
            item.when_was_found = item.when_was_found.strftime("%m/%d/%Y")
            item.withdrawal_deadline = item.withdrawal_deadline.strftime(
                "%m/%d/%Y")
            item.shift = item.shift
            item.status = self.STATUS_CHOICES[item.status]

        context['object_list'] = context_list
        context.update({'activeTab': 'delivered-items'})

        return context


class ExpiredItemsView(ListView):
    template_name = 'expired_items.html'
    allow_empty = True
    queryset = Item.objects.all().filter(status='Expired')

    STATUS_CHOICES = {
        'Lost': 'Perdido',
        'Delivered': 'Entregue',
        'Expired': 'Expirado'
    }

    def get_context_data(self, **kwargs):
        context = super(ExpiredItemsView, self).get_context_data(**kwargs)
        context_list = context['object_list']

        for item in context_list:
            item.when_was_found = item.when_was_found.strftime("%m/%d/%Y")
            item.withdrawal_deadline = item.withdrawal_deadline.strftime(
                "%m/%d/%Y")
            item.shift = item.shift
            item.status = self.STATUS_CHOICES[item.status]

        context['object_list'] = context_list
        context.update({'activeTab': 'expired-items'})

        return context


class ItemCreate(CreateView):
    model = Item
    form_class = ItemModelForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('items')

    def get(self, request):
        if (isAuthenticated(request)):
            return redirect(reverse_lazy('login'))

        return render(request, 'create_post.html', {'form': self.get_form(), 'activeTab': 'items'})

    def form_valid(self, form):
        user = self.request.session.get('user')
        form.instance.user_registration = user['registration']
        return super(ItemCreate, self).form_valid(form)


class ItemUpdate(UpdateView):
    model = Item
    form_class = ItemModelForm
    success_url = reverse_lazy('items')
    template_name = 'create_post.html'

    def get(self, request, pk):
        if (isAuthenticated(request)):
            return redirect(reverse_lazy('login'))

        item = get_object_or_404(Item, pk=pk)
        item.when_was_found = item.when_was_found.strftime("%d/%m/%Y")
        item.withdrawal_deadline = item.withdrawal_deadline.strftime("%d/%m/%Y")
        item.image.name = item.image.name[6:]

        form = ItemModelForm(instance=item)
        return render(request, 'create_post.html', {'form': form, 'item': item, 'activeTab': 'items', })


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy("items")
    template_name = "delete_post.html"


class CompleteDelivery(CreateView):
    model = DeliveredItem
    form_class = CompleteDeliveryModelForm
    template_name = 'complete_delivery.html'
    success_url = reverse_lazy('items')

    def form_valid(self, form):
        print("aaaaaaaaaaaa", self.kwargs['pk'])
        item = get_object_or_404(Item, id=self.kwargs['pk'])
        claimant_name = form.cleaned_data['claimant_name']
        cpf = form.cleaned_data['cpf']
        

        with transaction.atomic():
            itemDelivered = Item.objects.select_for_update().get(id=self.kwargs['pk'])
            itemDelivered.status = 'Delivered'
            itemDelivered.save()

        DeliveredItem.objects.create(item_id=item, claimant_name=claimant_name, cpf=cpf)
        return redirect(reverse_lazy('items'))

    # def save_form(self):
    #     pass

    def get(self, request, pk):
        if (isAuthenticated(request)):
            return redirect(reverse_lazy('login'))

        item = get_object_or_404(Item, pk=pk)
        item.when_was_found = item.when_was_found.strftime("%d/%m/%Y")
        
        form = self.get_form()

        return render(request, 'complete_delivery.html', { 'form': form, 'activeTab': 'items', 'item': item })

    # def get(self, request, pk):
    #     if (isAuthenticated(request)):
    #         return redirect(reverse_lazy('login'))

    #     item = get_object_or_404(Item, pk=pk)
    #     item.when_was_found = item.when_was_found.strftime("%d/%m/%Y")
    #     form = self.get_context_data()
    #     print("ESSA BUCTA AQUI", form)
    #     return render(request, 'complete_delivery.html', { 'form': form })