from django.contrib.auth.models import User

import django_filters
from rest_framework import (filters, permissions, viewsets,)

from api.models import Provider, ServiceArea
from api.permissions import IsOwnerOrReadOnly
from api.serializers import (ProviderSerializer,
                             ServiceAreaSerializer,
                             UserSerializer,)

class UserViewSet(viewsets.ModelViewSet):
    """
    ### This view provide `retrieve`, `create`, `list` and `options` methods.

    You need create new users to use all the functionality in this API
    You could make a post with the following data

        Request
            Method
                POST
            Headers
                Content-Type: application/json
            Data
                {
                    "first_name": "Jhon",
                    "last_name": "Doe",
                    "username": "Jdoe",
                    "password": "my_password"
                }
    """
    queryset = User.objects.filter(is_staff=False,
                                   is_superuser=False,
                                   is_active=True)
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, IsOwnerOrReadOnly,)

    def metadata(self, request):
        """
        Don't include the view description in OPTIONS responses.
        """
        data = super(UserViewSet, self).metadata(request)
        data.pop('name')
        data.pop('description')
        data.pop('renders')
        data.pop('parsers')
        return data



class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    filter_fields = ('name', 'email',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ServiceAreaFilter(filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')
    provider = django_filters.CharFilter(name="provider__name")

    class Meta:
        model = ServiceArea
        fields = ['name', 'price', 'area', 'provider', 'min_price', 'max_price']


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    # filter_fields = ('name', 'price', 'area', 'provider',)
    filter_class = ServiceAreaFilter

    def perform_create(self, serializer):
        provider = Provider.objects.get(user=self.request.user)
        serializer.save(provider=provider)
