from django.db import models
from restaurant.models import Customer,Restaurant
from django.db.models.signals import post_save
from django.dispatch import receiver

from restaurant.models import User

class Notification(models.Model):
    title = models.CharField(max_length=256,null=True)
    order = models.TextField(null=True)
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    curr_user = models.TextField(max_length=30)
    dest_user = models.ForeignKey(User, on_delete=models.CASCADE)
    types = [('GENERAL', 'General'), ('ORDER', 'Order'), ('PAYMENT', 'Payment'), ('App','App')]
    type = models.CharField(max_length=8, choices=types, default="PERSONAL")


@receiver(post_save, sender=User)
def create_welcome_message(sender, **kwargs):
    if kwargs.get('created', False):
        Notification.objects.create(dest_user=kwargs.get('instance'),
                                    title="Welcome to our RESTFO site!",
                                    message="Thanks for signing up!",
                                    curr_user="RESTFO",type="App")
