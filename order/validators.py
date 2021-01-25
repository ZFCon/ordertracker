from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class HasDoderValidator:
    requires_context = True

    def __init__(self, field):
        self.field = field

    def get_value(self, attrs):
        for attr in attrs.items():
            name, value = attr
            if name == self.field:
                return value

    def get_method(self, serializer):
        request = serializer.context['request']

        return request.method

    def __call__(self, attrs, serializer):
        method = self.get_method(serializer)

        if method == 'POST':
            order = self.get_value(attrs)

            if order.doer:
                raise ValidationError(_('This order has doer already.'))

    def __repr__(self):
        return '<%s(field=%s)>' % (
            self.__class__.__name__,
            self.field
        )
