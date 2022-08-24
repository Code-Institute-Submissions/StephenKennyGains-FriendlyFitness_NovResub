""" Allows adding Cartconfig to Cart """
from django.apps import AppConfig


class CartConfig(AppConfig):
    """ Sets cart confif to cart app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
