from markdown import markdown
from math import floor, ceil

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from .category import Category


class ArticleQuerySet(models.QuerySet):
    def slug(self, slug: str):
        return self.filter(slug=slug)

    def published(self):
        return self.filter(publish=True)

    def user(self, user: User):
        return self.filter(user_id=user.pk)

    def category(self, category: Category):
        return self.filter(category_id=category.pk)

    def search(self, search: str):
        if search:
            return self.filter(Q(title__icontains=search) | Q(content__icontains=search))
        return self


class BaseArticleManager(models.Manager):
    def get_object_or_none(self, id: int):
        try:
            return self.get(pk=id)
        except self.model.DoesNotExist:
            return None


ArticleManager = BaseArticleManager.from_queryset(ArticleQuerySet)


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

    def __str__(self):
        return f'#{self.pk} {self.title}'

    def content_reading_time_minutes(self):
        words_count = len(str(self.content).split(' '))
        minutes = floor(words_count / 200) + ceil(((words_count / 200) % 1) * 0.6)
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
