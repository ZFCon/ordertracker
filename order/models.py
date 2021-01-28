from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Status(models.TextChoices):
    PENDING = 'pending', _('Pending')
    ACCEPTED = 'accepted', _('Accepted')
    REFUSED = 'refused', _('Refused')


class DoerRequest(models.Model):
    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, related_name='requests', validators=[])

    status = models.CharField(
        max_length=25, choices=Status.choices, default=Status.PENDING)

    doer = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_status_display()


class Order(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='orders')
    request = models.TextField(help_text=_('Say what you want.'))

    created = models.DateTimeField(auto_now_add=True)

    @property
    def doer(self):
        doer = None
        request = self.requests.filter(
            status=Status.ACCEPTED).first()

        if(request):
            doer = request.doer

        return doer

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return self.request
