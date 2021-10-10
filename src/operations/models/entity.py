from functools import wraps
from typing import Callable

from django.db import models
from django.utils.translation import gettext_lazy as _


def save_and_refresh(method: Callable):
    @wraps(method)
    def wrap(self):
        method(self)
        self.save()
        return type(self).objects.get(id=self.id)

    return wrap


class Entity(models.Model):
    created = models.DateTimeField(
        auto_now_add=True, help_text=_('created'), verbose_name=_('created')
    )
    modified = models.DateTimeField(
        auto_now=True, help_text=_('modified'), verbose_name=_('modified')
    )

    class Meta:
        abstract = True
