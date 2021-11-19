from django.contrib import admin

from .models.product_category import ProductCategory
from .models.publication import Publication

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Publication)