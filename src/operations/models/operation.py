from typing import Tuple

from django.db import models
from django.utils.translation import gettext_lazy as _

from .entity import Entity


class Operation(Entity):
    DEPOSIT: str = 'DEPOSIT'
    WITHDRAW: str = 'WITHDRAW'
    OPERATIONS: Tuple = (
        (DEPOSIT, DEPOSIT),
        (WITHDRAW, WITHDRAW),
    )
    user = models.ForeignKey(
        to='operations.User',
        verbose_name=_('user'), help_text=_('user'),
        on_delete=models.CASCADE, related_name='operations',
    )
    type_operation = models.CharField(
        verbose_name=_('status'), help_text=_('status'),
        max_length=18, choices=OPERATIONS, default=WITHDRAW,
    )
    amount = models.DecimalField(
        verbose_name=_('amount'), help_text=_('amount'),
        max_digits=8, decimal_places=2,
    )

    class Meta:
        verbose_name = _('operation')
        verbose_name_plural = _('operations')
        db_table = 'operations_operation'
