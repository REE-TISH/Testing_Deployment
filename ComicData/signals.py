from django.db.models.signals import post_save  
from django.dispatch import receiver
from .models import Comic,ComicGroup

@receiver(post_save, sender=Comic)
def comic_saved(sender, instance, created, **kwargs):
    if created:
        ComicGroup.objects.create(name=f"{instance.title} Chat Group", avatar=instance.cover_image)

