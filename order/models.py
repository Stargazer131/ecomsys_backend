from django.db import models


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='orders') 
    status_choices = [
        ('C', 'Canceled'),
        ('A', 'Arrived'),
        ('T', 'Transporting'),
        ('H', 'Hold'),
    ]
    status = models.CharField(max_length=1, choices=status_choices)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    class Meta:
        app_label = 'user' # app_label helps django to recognize your db
        db_table = 'orders'
        ordering = ['-created_timestamp']