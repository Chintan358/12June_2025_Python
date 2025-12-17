
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from myapp.models import *

@receiver(post_save,sender=Faculty)
def test(sender, instance, created, **kwargs):
    print(created)
    print(sender)
    print("Calling")