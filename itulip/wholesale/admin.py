from django.contrib import admin

from wholesale.models import *

# Register your models here.

admin.site.register(Orders)
admin.site.register(OrderDetails)
admin.site.register(Clients)
admin.site.register(Sorts)