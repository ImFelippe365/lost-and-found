from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemModelForm, CompleteDeliveryModelForm
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Item, DeliveredItem, Claimant
from core.models import User
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib import messages

def isAuthenticated(request):
    token = request.session.get('token')
    if (token is None):
        return True
    return False


class ItemsView(ListView):
    template_name = 'items.html'
    allow_empty = True
    queryset = Item.objects.all().filter(status='Lost')
    ordering = ['-id']

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
        messages.success(self.request, 'Sua ação foi realizada com êxito')

        return context


class DeliveredItemsView(ListView):
    template_name = 'delivered_items.html'
    allow_empty = True
    queryset = Item.objects.all().filter(status='Delivered')
    ordering = ['-id']

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
    ordering = ['-id']

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


class CreateItemView(CreateView):
    model = Item
    form_class = ItemModelForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('items')

    def get(self, request):
        if (isAuthenticated(request)):
            return redirect(reverse_lazy('login'))

        return render(request, 'create_post.html', {'form': self.get_form(), 'activeTab': 'items'})

    def form_valid(self, form):
        instance = form.save(commit=False)
        user_object = self.request.session.get('user')
        user, user_created = User.objects.get_or_create(registration=user_object['registration'], defaults=user_object)
        instance.created_by = user

        messages.success(self.request, 'Sua ação foi realizada com êxito')

        return super(CreateItemView, self).form_valid(form)


class UpdateItemView(UpdateView):
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

        if item.status == 'Delivered':
            return redirect(reverse_lazy('items'))

        form = ItemModelForm(instance=item)

        return render(request, 'create_post.html', {'form': form, 'item': item, 'activeTab': 'items', })

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Sua ação foi realizada com êxito')
        return super().form_valid(form)


class DeleteItemView(DeleteView):
    model = Item
    success_url = reverse_lazy("items")
    template_name = "delete_post.html"

    def form_valid(self, form):
        self.object.delete()
        messages.success(self.request, 'Sua ação foi realizada com êxito')
        return redirect(reverse_lazy('items'))

    def get(self, request, pk):
        if (isAuthenticated(request)):
            return redirect(reverse_lazy('login'))

        item = get_object_or_404(Item, pk=pk)
        if item.status == 'Delivered':
            return redirect(reverse_lazy('items'))

        item.when_was_found = item.when_was_found.strftime("%d/%m/%Y")
        
        form = self.get_form()

        return render(request, 'delete_post.html', { 'form': form, 'activeTab': 'items', 'object': item })


class CompleteDeliveryView(CreateView):
    model = DeliveredItem
    form_class = CompleteDeliveryModelForm
    template_name = 'complete_delivery.html'
    success_url = reverse_lazy('items')

    def form_valid(self, form):
        item = get_object_or_404(Item, id=self.kwargs['pk'])
        name = form.cleaned_data['name']
        cpf = form.cleaned_data['cpf']

        user_object = self.request.session.get('user')

        claimant, claimant_created = Claimant.objects.get_or_create(cpf=cpf, defaults={'name': name})
        user, user_created = User.objects.get_or_create(registration=user_object['registration'], defaults=user_object)
        
        with transaction.atomic():
            itemDelivered = Item.objects.select_for_update().get(id=self.kwargs['pk'])
            itemDelivered.status = 'Delivered'
            itemDelivered.save()

        DeliveredItem.objects.create(item=item, claimant=claimant, user=user)
        messages.success(self.request, 'Sua ação foi realizada com êxito')

        return redirect(reverse_lazy('items'))

    def get(self, request, pk):
        if (isAuthenticated(request)):
            return redirect(reverse_lazy('login'))

        item = get_object_or_404(Item, pk=pk)
        if item.status == 'Delivered':
            return redirect(reverse_lazy('items'))

        item.when_was_found = item.when_was_found.strftime("%d/%m/%Y")
        
        form = self.get_form()

        return render(request, 'complete_delivery.html', { 'form': form, 'activeTab': 'items', 'item': item })