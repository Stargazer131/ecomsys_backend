from django.shortcuts import get_object_or_404
from cart.models import CartItem
import random


CART_ID_SESSION_KEY = 'cart_id'


# Get the current user's cart id; set a new one if blank
def get_cart_id(request):
    if not request.session.get(CART_ID_SESSION_KEY, ''):
        request.session[CART_ID_SESSION_KEY] = generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]


# Generate a random cart id
def generate_cart_id():
    cart_id = ''
    characters = '!#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    cart_id_length = 50
    for _ in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id


# Return all items from the current user's cart
def get_cart_items(request):
    return CartItem.objects.filter(cart_id=get_cart_id(request))


# Add an item to the cart
def add_to_cart(request):
    post_data = request.POST.copy()
    quantity = 1
    product_id = int(post_data.get('product_id'))
    cart_products = get_cart_items(request)
    product_in_cart = False

    # Check to see if the item is already in the cart
    for cart_item in cart_products:
        if cart_item.product_id == product_id:
            # Update the quantity if found
            cart_item.augment_quantity(quantity)
            product_in_cart = True

    if not product_in_cart:
        # Create and save a new cart item
        ci = CartItem()
        ci.id = random_id()
        ci.quantity = quantity
        ci.cart_id = get_cart_id(request)
        ci.product_id = product_id
        ci.save()


# Returns the total number of items in the user's cart
def cart_distinct_item_count(request):
    return get_cart_items(request).count()


def get_single_item(cart_item_id):
    return get_object_or_404(CartItem, id=cart_item_id)


def update_cart(request):
    post_data = request.POST.copy()
    cart_item_id = int(post_data['cart_item_id'])
    quantity = int(post_data['quantity'])
    cart_item = get_single_item(cart_item_id)

    if cart_item:
        if int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
        else:
            remove_from_cart(request)


def remove_from_cart(request):
    post_data = request.POST.copy()
    cart_item_id = int(post_data['cart_item_id'])
    cart_item = get_single_item(cart_item_id)

    if cart_item:
        cart_item.delete()


def random_id():
    id_list = CartItem.objects.values_list('id', flat=True)
    while True:
        id = random.randint(1, 1_000_000_000)
        if id not in id_list:
            break
    return id
        