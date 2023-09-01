import random

from django.db import models
from django.utils import timezone


class Order(models.Model):
    """Order model for Omni API."""
    class Statuses(models.TextChoices):
        NEW = "1", "Новий"
        INPOST = "2", "Розміщений у поштомат"
        SUCCES = "3", "Отриманий клієнтом"
        DECLINE = "4", "Відмова"

    status = models.IntegerField(choices=Statuses.choices, default=Statuses.NEW)
    number = models.IntegerField(unique=True, primary_key=True)
    where_from = models.TextField()
    where_to = models.TextField()
    create_date = models.DateTimeField(default=timezone.now, blank=True)
    update_date = models.DateTimeField(default=timezone.now, blank=True)

    def change_status(self):
        if self.status == self.Statuses.NEW:
            self.status = self.Statuses.INPOST
        elif self.status == self.Statuses.INPOST:
            self.status = random.choice((self.Statuses.SUCCES,self.Statuses.DECLINE))
        self.update_date = timezone.now()
        self.save()
