from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.apps import apps


class HaveOrderValidator:
    def __call__(self, order):
        if order.doer:
            raise ValidationError(_('This order has doer already.'))
        else:
            pass
