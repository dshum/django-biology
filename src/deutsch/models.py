from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class WordList(models.Model):
    class Meta:
        verbose_name_plural = _('Word lists')
        ordering = ['order']

    class Language(models.TextChoices):
        ENGLISH = 'en', _('English')
        GERMAN = 'de', _('German')

    title = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, blank=True, null=True, default=None)
    language = models.CharField(choices=Language.choices, default=Language.GERMAN)
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        db_index=True,
        related_name='word_lists'
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.title}'


class ListCategory(models.Model):
    class Meta:
        verbose_name_plural = _('List categories')
        ordering = ['order']

    title = models.CharField(max_length=255)
    word_list = models.ForeignKey(
        WordList,
        on_delete=models.PROTECT,
        db_index=True,
        related_name='categories'
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.title}'


class Word(models.Model):
    class Meta:
        verbose_name_plural = _('Words')
        ordering = ['word']

    word = models.CharField(max_length=255)
    translated_word = models.CharField(max_length=255, null=True, default=None)
    word_list = models.ForeignKey(
        WordList,
        blank=True,
        null=True,
        default=None,
        on_delete=models.PROTECT,
        db_index=True,
        related_name='words'
    )
    list_category = models.ForeignKey(
        ListCategory,
        blank=True,
        null=True,
        default=None,
        on_delete=models.PROTECT,
        db_index=True,
        related_name='words'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
