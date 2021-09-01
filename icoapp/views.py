from rest_framework import generics, status
from rest_framework.response import Response

from .models import Monitor, Bid, Allocation
from .serializers import MonitorSerializer, AllocationSerializer, BidSerializer


class CreateBid(generics.CreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exceptions=True):
            return Response({"message": "Something went wrong. Please try again later"},
                            status=status.HTTP_400_BAD_REQUEST)

        creation_date = request.data.get('timestamp')

        bidding_window = Monitor.objects.first()
        bidding_window = bidding_window

        if creation_date < bidding_window and serializer.is_valid():
            serializer.save(timestamp=creation_date)
            return Response({"message": "Your bid has been successfully created"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Sorry! The bidding window has closed. You cannot place a bid at this time"},
                            status=status.HTTP_400_BAD_REQUEST)


class DetailBid(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class AllBids(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
