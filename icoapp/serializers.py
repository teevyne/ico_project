from rest_framework import serializers
from .models import Allocation, Bid, BidMonitor


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'


class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = ('bid_id', 'number_of_token_received')


class BidMonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidMonitor
        fields = '__all__'


class BidAllocationSerializer(serializers.ModelSerializer):
    bid_object = AllocationSerializer(many=False)

    class Meta:
        model = Bid
        fields = ['id', 'user_id', 'bidding_price', 'number_of_tokens', 'timestamp', 'bid_object']
