from django.contrib.gis import admin
from models import Provider, ServiceArea

admin.site.register(Provider, admin.ModelAdmin)
admin.site.register(ServiceArea, admin.GeoModelAdmin)
