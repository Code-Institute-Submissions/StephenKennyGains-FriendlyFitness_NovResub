""" Cart View """
from django.shortcuts import (render, redirect,
                              reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from services.models import Service

# Create your views here.


def view_cart(request):
    """ A view to return Shopping Cart Page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ A item or items to Shopping Cart """

    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Great! Added {service.name} to your cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Great! Added {service.name} to your Cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    service = get_object_or_404(Service, pk=item_id)

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'You Updated {service.name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'You Removed {service.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        service = get_object_or_404(Service, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        request.session['cart'] = cart
        messages.success(request, f'You Removed {service.name} from your cart')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing service: {e}')
        return HttpResponse(status=500)
