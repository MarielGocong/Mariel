from django.contrib import admin
from .models import CustomerBook, HairServices, NailServices, Package

admin.site.register(CustomerBook)
admin.site.register(HairServices)
admin.site.register(NailServices)
admin.site.register(Package)


