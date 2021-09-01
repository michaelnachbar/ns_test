from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Product(models.Model):
    product_code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    unit_price = models.DecimalField(decimal_places=2,max_digits=8)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    def get_absolute_url(self):
        return reverse('product', kwargs={'product_code': self.product_code})
    

class Category(models.Model):
    category_code = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)
    def __str__(self):
        return self.category_name
    def get_absolute_url(self):
        return reverse('categories', kwargs={'category_code': self.category_code})
