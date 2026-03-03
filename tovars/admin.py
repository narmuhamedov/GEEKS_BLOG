from django.contrib import admin
from tovars.models import SerialNumber, Product, ReviewProduct, Tag

admin.site.register(SerialNumber)
admin.site.register(Product)
admin.site.register(ReviewProduct)
admin.site.register(Tag)