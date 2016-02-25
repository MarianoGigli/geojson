from django.conf.urls import url

from api.views import ProviderViewSet, ServiceAreaViewSet, UserViewSet

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

provider_list = ProviderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

provider_detail = ProviderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

service_area_list = ServiceAreaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

service_area_detail = ServiceAreaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^user/$', user_list, name=u'user-list'),
    url(r'^user/(?P<pk>[0-9]+)/$', user_detail, name=u'user-detail'),
    url(r'^provider/$', provider_list, name=u'provider-list'),
    url(r'^provider/(?P<pk>[0-9]+)/$',
        provider_detail,
        name=u'provider-detail'),
    url(r'^service-area/$', service_area_list, name=u'service-area-list'),
    url(r'^service-area/(?P<pk>[0-9]+)/$',
        service_area_detail,
        name=u'service-area-detail'),
]
