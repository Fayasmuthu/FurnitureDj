from django.contrib import admin
from .models import Product,Carousel,Order,Orderitem
# Register your models here.
class OrderitemTubleInline(admin.TabularInline):
    model=Orderitem
class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderitemTubleInline]

admin.site.register(Product)
admin.site.register(Carousel)
admin.site.register(Order,OrderAdmin)
admin.site.register(Orderitem)