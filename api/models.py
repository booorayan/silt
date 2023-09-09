from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Order {self.id} for {self.customer.name}'
