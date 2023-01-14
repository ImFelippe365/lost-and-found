import datetime
from ..models import Item
from django.db import transaction


def set_item_status():
    items = Item.objects.all().filter(status='Lost')
    print('item scheduler')
    with transaction.atomic():
        for item in items:
            print(item)
            if datetime.date.today() > item.withdrawal_deadline:
                print('entrou')
                item.status = 'Expired'
                item.save()