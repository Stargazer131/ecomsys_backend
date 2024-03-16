from cart.models import CartItem
from user.models import User


# Return all items from the current user's cart
def get_cart_items(user_id):
    user = User.objects.get(id=user_id)
    cart_items = user.cart_items.all() 
    return cart_items


# Add an item to the cart
def add_to_cart(product_id, user_id):
    cart_products = get_cart_items(user_id)
    product_in_cart = False

    for cart_item in cart_products:
        if cart_item.product_id == product_id:
            cart_item.augment_quantity(1)
            product_in_cart = True

    if not product_in_cart:
        ci = CartItem()
        ci.quantity = 1
        ci.user = User.objects.get(id=user_id)
        ci.product_id = product_id
        ci.save()


# Returns the total number of items in the user's cart
def cart_distinct_item_count(request):
    return get_cart_items(request).count()


def get_single_item(cart_item_id):
    return CartItem.objects.get(id=cart_item_id)


def update_cart(cart_item_id, quantity):
    cart_item = get_single_item(cart_item_id)

    if cart_item:
        if int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
        else:
            remove_from_cart(cart_item_id)


def remove_from_cart(cart_item_id):
    cart_item = get_single_item(cart_item_id)
    if cart_item:
        cart_item.delete()

        