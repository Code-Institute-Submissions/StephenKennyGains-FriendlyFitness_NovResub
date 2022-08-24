""" Checkout Configuration """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """Checkout Configuration """
    name = 'checkout'

    def ready(self):
        import checkout.signals
