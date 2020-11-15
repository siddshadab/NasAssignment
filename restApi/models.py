from django.db import models
from django.utils.translation import gettext_lazy as _


class CheckOutSystem(models.Model):
    slot_number = models.CharField(_('slot_number'), max_length=2)
    objects = models.Manager()


class SlotMaster(models.Model):
    id = models.AutoField(_('id'), auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(_('name'), max_length=20, default='', null=True)
    is_slot_available = models.CharField(_('is_slot_available'), max_length=2, default=0, null=True)
    objects = models.Manager()


class ParkingSystem(models.Model):
    car_number = models.CharField(_('car_number'), max_length=20)
    customer_name = models.CharField(_('customer_name'), max_length=150, blank=True)
    contact_no = models.CharField(_('contact_no'), max_length=10, blank=True)
    in_date_time = models.DateTimeField(_('in_date_time'), null=True, auto_now_add=True)
    out_date_time = models.DateTimeField(_('out_date_time'), null=True, auto_now_add=True)
    slot_number = models.CharField(_('slot_number'), max_length=2)
    is_checked_out = models.CharField(_('is_checked_out'), max_length=2)
    objects = models.Manager()
