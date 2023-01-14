import datetime
from ..models import Item
from django.db import transaction


def set_item_status():
    items = Item.objects.all().filter(status='Lost')
    with transaction.atomic():
        for item in items:
            if datetime.date.today() > item.withdrawal_deadline:
                item.status = 'Expired'
                item.save()