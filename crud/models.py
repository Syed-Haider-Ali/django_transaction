from django.db import models


class TimeStapms(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
        abstract = True

class Product(TimeStapms):
    name = models.CharField(max_length=200)
    description = models.TextField()
    manufacturing_date = models.DateField()

class Images(TimeStapms):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='images/')


