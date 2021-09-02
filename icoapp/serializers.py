from rest_framework import serializers
from .models import Allocation, Bid, BidMonitor


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'


class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = '__all__'


class BidMonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidMonitor
        fields = '__all__'
