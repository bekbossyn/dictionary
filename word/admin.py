from django.contrib import admin

from .models import Word, Language


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'data', 'timestamp',)

    ordering = ('-timestamp',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'code_name', 'display_name', 'timestamp',)

    search_fields = ('code_name', 'display_name',)

    ordering = ('-timestamp',)
