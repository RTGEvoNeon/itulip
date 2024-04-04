from django.contrib import admin

from wholesale.models import *

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Client)
admin.site.register(Sort)