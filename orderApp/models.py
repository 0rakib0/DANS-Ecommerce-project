from django.db import models
from Accounts.models import User
from shopApp.models import Product



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card')
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    color = models.CharField(max_length=50, default='no color selected')
    size = models.CharField(max_length=50, default='free size')
    purchase = models.BooleanField(default=False)
    createAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return str(self.quantity) + ' X ' + str(self.item)
    

    def get_total(self):

        if self.item.dic_price == 0:
            total = self.item.main_price * self.quantity
        else:
            total = self.item.dic_price * self.quantity
        
        floatTotal = format(total, '0.2f')

        return floatTotal
    

class Order(models.Model):
    orderItem = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
    ordered = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    order_date = models.DateField(auto_now=True)
    paymentId = models.CharField(max_length=264, blank=True, null=True)
    delivered_status = models.BooleanField(default=False)
    orderId = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.user.email)+ "'s order"
    
    def save(self, *args, **kwargs):
        # Extract only the date part from createdAt field
        if self.createdAt:
            self.createdAt = self.createdAt.date()
        super(Order, self).save(*args, **kwargs)
    

    def getTotals(self):
        total = 0
        for order_item in self.orderItem.all():
            total += float(order_item.get_total())
        return total
