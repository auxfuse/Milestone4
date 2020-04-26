from django.db import models
from django.contrib.auth.models import User
from membership.models import Membership
from django.utils import timezone


# Models
class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user}, {self.order_date}'


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, null=False,
                                   on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=False)

    def __str__(self):
        return f'{self.quantity} {self.membership.type} @ ' \
               f'{self.membership.price}'
