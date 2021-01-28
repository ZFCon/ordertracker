from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Status


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


class StatusHasDoderValidator:
    requires_context = True

    def __init__(self, field):
        self.field = field

    def is_update(self, serializer):
        request = serializer.context['request']

        return request.method in ['PATCH', 'PUT']

    def get_value(self, attrs):
        for attr in attrs.items():
            name, value = attr
            if name == self.field:
                return value

    def has_doer(self, serializer):
        instance = serializer.instance

        return instance.doer is not None

    def __call__(self, attrs, serializer):
        is_update = self.is_update(serializer)

        if is_update:
            has_doer = self.has_doer(serializer)
            value = self.get_value(attrs)

            if (value == Status.ACCEPTED) and has_doer:
                raise ValidationError(
                    _("you can't accept this request because this order already had a doer."))

    def __repr__(self):
        return '<%s(field=%s)>' % (
            self.__class__.__name__,
            self.field
        )
