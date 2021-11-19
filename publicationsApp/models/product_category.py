# Create a Product Category model
from django.db import models

class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='app/category/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name