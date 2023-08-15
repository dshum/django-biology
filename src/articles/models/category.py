from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryQuerySet(models.QuerySet):
    def category(self, parent):
        return self.filter(parent_category=parent)


class BaseCategoryManager(models.Manager):
    def get_object_or_none(self, id: int):
        try:
            return self.get(pk=id)
        except self.model.DoesNotExist:
            return None


CategoryManager = BaseCategoryManager.from_queryset(CategoryQuerySet)


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
