from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "status"]
    list_editable = ["user", "status"]


admin.site.register(Order)
admin.site.register(OrderItem)
