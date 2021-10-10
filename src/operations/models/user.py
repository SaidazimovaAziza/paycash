from django.db import models
from django.utils.translation import gettext_lazy as _

from .entity import Entity


class User(Entity):
    username = models.CharField(
        verbose_name=_('username'), help_text=_('username'),
        max_length=25,
    )
    email = models.CharField(
        verbose_name=_('email'), help_text=_('email'),
        max_length=25,
    )

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'operations_user'
