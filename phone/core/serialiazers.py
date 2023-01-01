from rest_framework import serializers

from phone.core.models import Phone


class PhoneSerializers(serializers.ModelSerializer):

    class  Meta:
        model = Phone
        fields = ('id', 'number',)