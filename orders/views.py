from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                            product=item['product'],
                            price=item['price'],
                            quantity=item['quantity'])
         # очистить корзину
            cart.clear()
            item_id = order.id + 1000
            return render(request,
                        'orders/created.html',
                        {'order': order,
                         'item_id': item_id })
    else:
        form = OrderCreateForm()
    return render(request,
                    'orders/create.html',
                    {'cart': cart, 'form': form})


