# -*- coding: utf-8 -*-
from django.contrib import admin

from locking.admin import LockableAdmin
from .models import Choice, Poll


class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ('votes',)
    extra = 3


class PollAdmin(LockableAdmin):
    fieldsets = [
        (None, {
            'fields': ['question'],
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'lock')
    search_fields = ['question']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
