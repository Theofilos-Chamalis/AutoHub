from django.contrib import admin
from .models import Seller, Category1, Category2, Category3
from .models import Manufacturer, Car, Category4, Category5


admin.site.register(Seller)
admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Category1)
admin.site.register(Category2)
admin.site.register(Category3)
admin.site.register(Category4)
admin.site.register(Category5)


