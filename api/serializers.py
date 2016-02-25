from django.contrib.auth.models import User
from rest_framework import serializers

from models import Provider, ServiceArea


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'username', 'password',)
        extra_kwargs = {
            'password': {'write_only': True},
            'url': {'read_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('url', 'name', 'email', 'phone', 'language',
                  'currency', 'user',)
        extra_kwargs = {
            'user': {'read_only': True},
            'url': {'read_only': True}
        }


class ServiceAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ('url', 'name', 'price', 'area', 'provider')
        extra_kwargs = {
            'url': {'view_name': 'service-area-detail', 'read_only': True},
            'provider': {'read_only': True}
        }
