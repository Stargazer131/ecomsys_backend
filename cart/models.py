from django.db import models


# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='cart_items')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='cart_items', 
                              null=True, default=None, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product_id = models.IntegerField()
    is_active = models.BooleanField(default=True)


    class Meta:
        app_label = 'user' # app_label helps django to recognize your db
        db_table = 'cart_items'
        ordering = ['-date_added']


    def augment_quantity(self, quantity):
        self.quantity += int(quantity)
        self.save()
        