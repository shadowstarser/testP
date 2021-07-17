from rest_framework import serializers
from tsevent.models import tsevent



class tseventDetailSerialazer(serializers.ModelSerializer):
    class Meta:
        model = tsevent
        fields = '__all__'

class tseventListSerialazer(serializers.ModelSerializer):
    class Meta:
        model = tsevent
        fields = '__all__'