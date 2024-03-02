from django.shortcuts import render
from cart.cart import add_to_cart, update_cart, remove_from_cart, get_cart_items


# Create your views here.
def show_cart(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            add_to_cart(request)
        elif action == 'update':
            update_cart(request)
        else:
            remove_from_cart(request)
    else:
        pass
    
    cart_items = get_cart_items(request)
    context = {
        'cart_items': cart_items
    }
        
    return render(request, 'cart/cart.html', context) 
