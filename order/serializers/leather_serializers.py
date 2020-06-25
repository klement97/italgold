from rest_framework.serializers import ModelSerializer

from order.models import Leather, LeatherSerial


class LeatherSerialSerializer(ModelSerializer):
    class Meta:
        model = LeatherSerial
        fields = ['id', 'name']


class LeatherSerializer(ModelSerializer):
    serial = LeatherSerialSerializer()

    class Meta:
        model = Leather
        fields = ['id', 'code', 'serial', 'image']
