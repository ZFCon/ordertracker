from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.apps import apps


class HasDoderValidator:
    def __init__(self, field):
        self.field = field

    def get_value(self, attrs):
        for attr in attrs.items():
            name, value = attr
            if name == self.field:
                return value

    def __call__(self, attrs):
        order = self.get_value(attrs)
        if order.doer:
            raise ValidationError(_('This order has doer already.'))
        else:
            pass

    def __repr__(self):
        return '<%s(field=%s)>' % (
            self.__class__.__name__,
            self.field
        )
