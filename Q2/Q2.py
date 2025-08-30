import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from Q2app.models import Book

@receiver(post_save, sender=Book)
def book_saved_receiver(sender, instance, created, **kwargs):
    print(f"[Receiver] running in thread: {threading.current_thread().name}")
    print(f"[Receiver] Book saved: {instance.title}")
