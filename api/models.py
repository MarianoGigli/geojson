from django.contrib.auth.models import User
from django.contrib.gis.db import models

from api.currency import CURRENCY

class Provider(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    language = models.CharField(max_length=256)
    currency = models.CharField(max_length=3, choices=CURRENCY, default='USD')
    user = models.OneToOneField(User, related_name=u'provider')
    objects = models.GeoManager()

    def __unicode__(self):
        return u'{} - {}'.format(self.name, self.email)


class ServiceArea(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(name=u'price',
                                max_digits=8,
                                decimal_places=2)
    area = models.PolygonField()
    provider = models.ForeignKey(Provider, related_name=u'service_area')
    objects = models.GeoManager()

    def __unicode__(self):
        return u'{}'.format(self.name)

