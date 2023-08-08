from slugify import slugify

from django.core.cache.utils import make_template_fragment_key
from django.core.cache import cache
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Article


@receiver(pre_save, sender=Article)
def article_pre_save_handler(sender, instance, **kwargs):
    instance.slug = slugify(instance.title, lowercase=True, max_length=50, separator='-')
    return instance


@receiver(post_save, sender=Article)
def article_save_handler(sender, created, instance, **kwargs):
    keys = [
        make_template_fragment_key('article_menu', vary_on=(instance.pk,)),
        make_template_fragment_key('article_details', vary_on=(instance.pk,)),
    ]
    cache.delete_many(keys)
    return instance
