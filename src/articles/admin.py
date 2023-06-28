from django.contrib import admin

from .models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'order',
        'user',
        'parent_category',
        'created_at',
    )
    search_fields = ('title',)
    ordering = ('order',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'order',
        'user',
        'category',
        'level',
        'reading_time_minutes',
        'views',
        'created_at',
    )
    search_fields = ('title', 'level')
    ordering = ('order',)
