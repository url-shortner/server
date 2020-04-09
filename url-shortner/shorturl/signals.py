from django.dispatch import Signal, receiver
from ipware.ip import get_ip

from shorturl.models import Transaction
from shorturl.serializers import TransactionSerializer

transaction_sig = Signal(providing_args=['request'])


@receiver(transaction_sig)
def transaction(sender, request, **kwargs):
    transaction = Transaction()

    transaction.key = kwargs['key']
    transaction.is_disabled = kwargs['disabled']
    transaction.ip_address = get_ip(request)
    transaction.user_agent = request.META['HTTP_USER_AGENT']

    transaction.save()
