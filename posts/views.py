from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemModelForm, CompleteDeliveryModelForm
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Item, DeliveredItem, Claimant
from core.models import User
from django.urls import reverse_lazy
from django.db import transaction
from django.db.models import Q
from django.contrib import messages
import datetime
from django.forms import ValidationError
import re


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

    def get_queryset(self):
        query = self.request.GET.get('order')
        order = '-id' if query == 'desc' else 'id'
        return Item.objects.filter(status='Lost').order_by(order) if query is not None else Item.objects.filter(status='Lost').order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(ItemsView, self).get_context_data(**kwargs)
        context_list = context['object_list']

        for item in context_list:
            item.updated_at = item.updated_at.strftime("%Y/%m/%d")
            item.when_was_found = item.when_was_found.strftime("%d/%m/%Y")
            item.withdrawal_deadline = item.withdrawal_deadline.strftime(
                "%d/%m/%Y")
            item.shift = item.shift
            item.status = self.STATUS_CHOICES[item.status]

        context['object_list'] = context_list
        context.update(
            {'activeTab': 'items', 'order': self.request.GET.get('order')})
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

    def get_queryset(self):
        query = self.request.GET.get('order')
        order = '-id' if query == 'desc' else 'id'
        return Item.objects.filter(status='Delivered').order_by(order) if query is not None else Item.objects.filter(status='Delivered').order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(DeliveredItemsView, self).get_context_data(**kwargs)
        context_list = context['object_list']

        for item in context_list:
            item.updated_at = item.updated_at.strftime("%Y/%m/%d")
            item.when_was_found = item.when_was_found.strftime("%d/%m/%Y")
            item.withdrawal_deadline = item.withdrawal_deadline.strftime(
                "%d/%m/%Y")
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

    def get_queryset(self):
        query = self.request.GET.get('order')
        order = '-id' if query == 'desc' else 'id'
        return Item.objects.filter(status='Expired').order_by(order) if query is not None else Item.objects.filter(status='Expired').order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(ExpiredItemsView, self).get_context_data(**kwargs)
        context_list = context['object_list']

        for item in context_list:
            item.updated_at = item.updated_at.strftime("%Y/%m/%d")
            item.when_was_found = item.when_was_found.strftime("%d/%m/%Y")
            item.withdrawal_deadline = item.withdrawal_deadline.strftime(
                "%d/%m/%Y")
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

        return render(request, 'create_post.html', {'form': self.get_form(), 'activeTab': 'items', 'actionTitle': 'Criar nova postagem'})

    def form_valid(self, form):
        today = datetime.date.today()
        when_was_found = form.cleaned_data['when_was_found']
        withdrawal_deadline = form.cleaned_data['withdrawal_deadline']

        if not when_was_found <= today:
            form.add_error("when_was_found", ValidationError("Insira uma data válida", code="invalid"))
        
        if not withdrawal_deadline >= today:
            form.add_error("withdrawal_deadline", ValidationError("Insira uma data válida", code="invalid"))

        if (not withdrawal_deadline >= today or not when_was_found <= today):
            return render(self.request, 'create_post.html', {'form': form, 'activeTab': 'items', 'actionTitle': 'Criar nova postagem'})
        
        instance = form.save(commit=False)
        user_object = self.request.session.get('user')
        user, user_created = User.objects.get_or_create(
            registration=user_object['registration'], defaults=user_object)
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
        item.when_was_found = item.when_was_found.strftime("%Y-%m-%d")
        item.withdrawal_deadline = item.withdrawal_deadline.strftime(
            "%Y-%m-%d")
        item.image.name = item.image.name[6:]

        if item.status == 'Delivered':
            return redirect(reverse_lazy('items'))

        form = ItemModelForm(instance=item)

        return render(request, 'create_post.html', {'form': form, 'item': item, 'activeTab': 'items', 'actionTitle': 'Editar postagem'})

    def form_valid(self, form):
        today = datetime.date.today()
        when_was_found = form.cleaned_data['when_was_found']
        withdrawal_deadline = form.cleaned_data['withdrawal_deadline']
        
        if not when_was_found <= today:
            form.add_error("when_was_found", ValidationError("Insira uma data válida", code="invalid"))
        
        if not withdrawal_deadline >= today:
            form.add_error("withdrawal_deadline", ValidationError("Insira uma data válida", code="invalid"))

        if (not withdrawal_deadline >= today or not when_was_found <= today):
            item = get_object_or_404(Item, pk=self.kwargs['pk'])
            return render(self.request, 'create_post.html', {'form': form,'item': item, 'activeTab': 'items', 'actionTitle': 'Editrar postagem'})

        self.object = form.save()

        if self.object.withdrawal_deadline > datetime.date.today():
            with transaction.atomic():
                self.object.status = 'Lost'
                item = Item.objects.select_for_update().get(
                    id=self.kwargs['pk'])
                item.save()
        
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
        if item.status == 'Delivered' or item.status == 'Expired':
            return redirect(reverse_lazy('items'))

        form = self.get_form()

        return render(request, 'delete_post.html', {'form': form, 'activeTab': 'items', 'object': item})


class CompleteDeliveryView(CreateView):
    model = DeliveredItem
    form_class = CompleteDeliveryModelForm
    template_name = 'complete_delivery.html'
    success_url = reverse_lazy('items')

    def form_valid(self, form):
        item = get_object_or_404(Item, id=self.kwargs['pk'])
        name = form.cleaned_data['name']
        cpf = form.cleaned_data['cpf']
        cpf = re.sub(r'\.|\-', '', cpf)

        '''verificar se apenas números foram inseridos'''

        user_object = self.request.session.get('user')

        claimant, claimant_created = Claimant.objects.get_or_create(
            cpf=cpf, defaults={'name': name})
        user, user_created = User.objects.get_or_create(
            registration=user_object['registration'], defaults=user_object)

        with transaction.atomic():
            itemDelivered = Item.objects.select_for_update().get(
                id=self.kwargs['pk'])
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

        return render(request, 'complete_delivery.html', {'form': form, 'activeTab': 'items', 'item': item})
