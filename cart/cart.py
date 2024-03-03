from cart.models import CartItem
import random


CART_ID_SESSION_KEY = 'cart_id'


# Generate a random cart id
def generate_cart_id():
    cart_id = ''
    characters = '!#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    cart_id_length = 50
    for _ in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id


# Return all items from the current user's cart
def get_cart_items(cart_id):
    return CartItem.objects.filter(cart_id=cart_id)


# Add an item to the cart
def add_to_cart(product_id, cart_id):
    cart_products = get_cart_items(cart_id)
    product_in_cart = False

    for cart_item in cart_products:
        if cart_item.product_id == product_id:
            cart_item.augment_quantity(1)
            product_in_cart = True

    if not product_in_cart:
        ci = CartItem()
        ci.id = random_id()
        ci.quantity = 1
        ci.cart_id = cart_id
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


def random_id():
    id_list = CartItem.objects.values_list('id', flat=True)
    while True:
        id = random.randint(1, 1_000_000_000)
        if id not in id_list:
            break
    return id
        