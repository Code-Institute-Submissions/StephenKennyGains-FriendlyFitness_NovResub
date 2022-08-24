""" Cart Tools is ised for calculating the services
muiltiplied by the quantity"""
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculates Sub total by multiplying service by quantity """
    return price * quantity
