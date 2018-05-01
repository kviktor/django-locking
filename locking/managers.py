# coding=utf-8
import datetime

from django.db.models import Q, Manager
from django.utils import timezone

from locking import LOCK_TIMEOUT
"""
    LOCKED
            if (timezone.now() - self.locked_at).seconds < LOCK_TIMEOUT:
            
            
            self.locked_at < (NOW - TIMEOUT)
"""


def point_of_timeout():
    delta = datetime.timedelta(seconds=LOCK_TIMEOUT)
    return timezone.now() - delta


class LockedManager(Manager):
    def get_queryset(self):
        timeout = point_of_timeout()
        return super(LockedManager, self).get_queryset().filter(
            _locked_at__gt=timeout, _locked_at__isnull=False)


class UnlockedManager(Manager):
    def get_queryset(self):
        timeout = point_of_timeout()
        return super(UnlockedManager, self).get_queryset().filter(
            Q(_locked_at__lte=timeout) | Q(_locked_at__isnull=True))
