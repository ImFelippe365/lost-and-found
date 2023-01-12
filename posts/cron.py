from django_cron import CronJobBase, Schedule
from .models import Item
from django.db import transaction
import datetime

class UpdateStatus(CronJobBase):
    RUN_AT_TIMES = ['00:00']
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'posts.update_status'   

    def do(self):
        items = Item.objects.all()
        for item in items:
            if item.status =='Lost':
                if datetime.date.today() > item.withdrawal_deadline:
                    with transaction.atomic():
                        #item_expired = Item.objects.select_for_update().get(id=item.id)
                        item.status = 'Expired'
                        item.save()
            elif item.status == 'Expired':
                if item.withdrawal_deadline > datetime.date.today():
                    with transaction.atomic():
                        #item_expired = Item.objects.select_for_update().get(id=item.id)
                        item.status = 'Lost'
                        item.save()
        