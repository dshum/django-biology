import math

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from markdown import markdown


class CategoryManager(models.Manager):
    pass


class Category(models.Model):
    class Meta:
        verbose_name_plural = _('Categories')
        ordering = ['order']

    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_category = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        db_index=True,
        related_name='sub_categories'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        db_index=True,
        related_name='article_categories'
    )

    objects = CategoryManager()

    def __str__(self):
        return f'#{self.pk} {self.title}'


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(publish=True)


class Article(models.Model):
    class Meta:
        verbose_name_plural = _('Articles')
        ordering = ['order']

    class Level(models.TextChoices):
        EASY = 'easy', _('Easy')
        MEDIUM = 'medium', _('Medium')
        HARD = 'hard', _('Hard')

    title = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True)
    content = models.TextField()
    level = models.CharField(choices=Level.choices, default=None)
    reading_time_minutes = models.SmallIntegerField(default=None)
    views = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        db_index=True,
        related_name='articles'
    )
    category = models.ForeignKey(
        Category,
        default=None,
        on_delete=models.PROTECT,
        db_index=True,
        related_name='articles'
    )

    objects = ArticleManager()

    def content_reading_time_minutes(self):
        words_count = len(str(self.content).split(' '))
        minutes = math.floor(words_count / 200) + math.ceil(((words_count / 200) % 1) * 0.6)
        return minutes

    def content_html(self):
        return markdown(str(self.content), extensions=[
            'fenced_code',
            'footnotes',
            'attr_list',
            'def_list',
            'tables',
            'abbr',
            'md_in_html'
        ])


class Image(models.Model):
    class Meta:
        verbose_name_plural = _('Images')
        ordering = ['-created_at']

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        db_index=True,
        related_name='images'
    )

    objects = models.Manager()
