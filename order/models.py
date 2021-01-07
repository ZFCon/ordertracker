from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Order(models.Model):
    request = models.TextField(help_text=_('Say what you want.'))
    doer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                             null=True, blank=True, help_text=_('This should have the user that agreed to do it.'))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return self.request
