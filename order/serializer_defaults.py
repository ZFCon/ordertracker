from .models import Order


class OrderUrlDefault:
    requires_context = True

    def get_order(self, id):
        return Order.objects.get(id=id)

    def __call__(self, serializer_field):
        view = serializer_field.context['view']
        kwargs = view.kwargs
        order_pk = kwargs['order_pk']

        return self.get_order(order_pk)

    def __repr__(self):
        return '%s()' % self.__class__.__name__
