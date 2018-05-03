# encoding: utf-8
from django.contrib import admin

from locking.admin import LockableAdmin
from story_app.models import Story


class StoryAdmin(LockableAdmin):
    list_display = ('lock', 'content', )
    list_display_links = ('content', )


admin.site.register(Story, StoryAdmin)
