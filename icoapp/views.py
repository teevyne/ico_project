import datetime

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BidMonitor, Bid, Allocation
from .serializers import BidMonitorSerializer, BidSerializer, BidAllocationSerializer, AllocationSerializer


class CreateBid(generics.CreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(
                {"message": "Something went wrong. Please try again later"},
                status=status.HTTP_400_BAD_REQUEST)

        creation_datetime = datetime.datetime.now()
        monitor = BidMonitor.objects.first()
        bidding_window = str(monitor.bidding_window)[:19]

        window = datetime.datetime.strptime(bidding_window, "%Y-%m-%d %H:%M:%S")

        if creation_datetime < window and serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Your bid has been successfully created on " + str(creation_datetime)},
                status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": "Sorry! The bidding window has closed. You cannot place a bid at this time"},
                status=status.HTTP_400_BAD_REQUEST)


class DetailBid(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class AllBids(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class CreateMonitor(generics.CreateAPIView):
    queryset = BidMonitor.objects.all()
    serializer_class = BidMonitorSerializer


class DetailMonitor(generics.RetrieveUpdateDestroyAPIView):
    queryset = BidMonitor.objects.all()
    serializer_class = BidMonitorSerializer


class AllBidMonitors(generics.ListAPIView):
    queryset = BidMonitor.objects.all()
    serializer_class = BidMonitorSerializer


class AllBidPostAuction(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidAllocationSerializer


class CreateAllocation(generics.CreateAPIView):
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer
