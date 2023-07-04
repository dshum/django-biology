from django.contrib import admin

from .models import WordList, ListCategory, Word


@admin.register(WordList)
class WordListAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'language',
        'user',
        'order',
        'created_at',
    )
    search_fields = ('title', 'slug', 'language')
    ordering = ('order',)


@admin.register(ListCategory)
class WordListAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'word_list',
        'order',
        'created_at',
    )
    search_fields = ('title',)
    ordering = ('order',)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = (
        'word',
        'translated_word',
        'list_category',
        'word_list',
        'created_at',
    )
    search_fields = ('word',)
    ordering = ('word',)
