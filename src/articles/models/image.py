from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class ImageQuerySet(models.QuerySet):
    def user(self, user: User):
        return self.filter(user_id=user.pk)

    def search(self, search: str):
        if search:
            return self.filter(Q(title__icontains=search) | Q(image__icontains=search))
        return self


class BaseImageManager(models.Manager):
    def get_object_or_none(self, id: int):
        try:
            return self.get(pk=id)
        except self.model.DoesNotExist:
            return None


ImageManager = BaseImageManager.from_queryset(ImageQuerySet)


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

    objects = ImageManager()

    def __str__(self):
        return f'#{self.pk} {self.title}'
