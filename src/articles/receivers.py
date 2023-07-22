from django.core.cache.utils import make_template_fragment_key
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Article


@receiver(post_save, sender=Article)
def article_save_handler(sender, created, instance, **kwargs):
    keys = [
        make_template_fragment_key('article_menu', vary_on=(instance.pk,)),
        make_template_fragment_key('article_details', vary_on=(instance.pk,)),
    ]
    cache.delete_many(keys)
    return instance
