from django_cron import CronJobBase, Schedule
from .models import Item
from django.db import transaction
import datetime

class UpdateStatus(CronJobBase):
    RUN_EVERY_MINS = 5
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'posts.update_status'   

    def do(self):
        items = Item.objects.filter(status='Lost')
        for item in items:
            if item.status =='Lost':
                if datetime.date.today() > item.withdrawal_deadline:
                    with transaction.atomic():
                        #item_expired = Item.objects.select_for_update().get(id=item.id)
                        item.status = 'Expired'
                        item.save()
        