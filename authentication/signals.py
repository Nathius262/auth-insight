"""from django.dispatch import receiver
from django.db.models.signals import post_save


#@receiver(post_save, sender=CustomUser)
def createUserProfile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)     """
