# coding=utf-8
from django.db import models
from locking import models as locking


class Story(locking.LockableModel):
    content = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'stories'
        app_label = 'story_app'


class Unlockable(models.Model):
    """
    This model serves to test that `utils.gather_lockable_models`
    actually does what it's supposed to.
    """
    content = models.TextField(blank=True)

    class Meta:
        app_label = 'story_app'
