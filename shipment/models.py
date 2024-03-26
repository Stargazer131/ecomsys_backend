from datetime import datetime, timedelta
from django.db import models


# Create your models here.
class Shipment(models.Model):
    shipping_methods = {
        "Standard": {
            "fullname": "Standard Shipping",
            "fee": 5.99,
            "estimate_shipping_day": 5,
        },
        "Air": {"fullname": "Air Freight", "fee": 29.99, "estimate_shipping_day": 2},
        "Sea": {"fullname": "Sea Freight", "fee": 19.99, "estimate_shipping_day": 14},
        "Express": {
            "fullname": "Express Shipping",
            "fee": 99.99,
            "estimate_shipping_day": 1,
        },
        "Truck": {
            "fullname": "Truck Delivery",
            "fee": 49.99,
            "estimate_shipping_day": 3,
        },
        "Mail": {"fullname": "Mail Delivery", "fee": 3.99, "estimate_shipping_day": 7},
        "Local": {
            "fullname": "Local Delivery",
            "fee": 0.99,
            "estimate_shipping_day": 2,
        },
    }
    shipping_methods_name_list = ['Standard', 'Air', 'Sea', 'Express', 'Truck', 'Mail', 'Local']
    shipping_method_choices = [(alias, details['fullname']) for alias, details in shipping_methods.items()]

    order = models.OneToOneField("Order", on_delete=models.CASCADE, primary_key=True)
    shipping_address = models.TextField()
    shipping_method = models.CharField(max_length=30, choices=shipping_method_choices)
    estimated_delivery_date = models.DateField()
    tracking_information = models.TextField(max_length=255)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    fee = models.DecimalField(max_digits=9, decimal_places=2)


    class Meta:
        app_label = "user"  # app_label helps django to recognize your db
        db_table = "shipments"
        ordering = ["-created_timestamp"]
        
        
    def save(self, *args, **kwargs):
        if self.created_timestamp is None:  # Only calculate estimated delivery date if the instance is being created
            shipping_method_details = self.shipping_methods.get(self.shipping_method)
            if shipping_method_details:
                estimate_shipping_day = shipping_method_details.get('estimate_shipping_day', 21)
                self.estimated_delivery_date = (datetime.now() + timedelta(days=estimate_shipping_day)).date()
                print(self.estimated_delivery_date)
                self.fee = shipping_method_details.get('fee', 1.99)
        super().save(*args, **kwargs)
