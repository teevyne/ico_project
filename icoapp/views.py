import datetime

from django.db.models import Max, Count
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Offering, Bid, Allocation, User
from .serializers import OfferingSerializer, BidSerializer, BidAllocationSerializer, AllocationSerializer, \
    UserSerializer


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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

        monitor = Offering.objects.first()
        open_bidding_window = str(monitor.bidding_window_open)[:19]
        close_bidding_window = str(monitor.bidding_window_closed)[:19]
        open_window = datetime.datetime.strptime(open_bidding_window, "%Y-%m-%d %H:%M:%S")
        close_window = datetime.datetime.strptime(close_bidding_window, "%Y-%m-%d %H:%M:%S")

        if open_window <= creation_datetime <= close_window:
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
    queryset = Offering.objects.all()
    serializer_class = OfferingSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(
                {"message": "Something went wrong. Please try again later"},
                status=status.HTTP_400_BAD_REQUEST)

        opening = str(request.data.get('bidding_window_open')).replace("T", " ")
        closing = str(request.data.get('bidding_window_closed')).replace("T", " ")
        open_window = datetime.datetime.strptime(opening, "%Y-%m-%d %H:%M")
        close_window = datetime.datetime.strptime(closing, "%Y-%m-%d %H:%M")

        if open_window >= close_window:
            return Response({"message": "Error! Offering closing date must be greater than opening date"},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({"message": "Offering successfully set. Bids to follow soon"}, status=status.HTTP_200_OK)


class DetailMonitor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offering.objects.all()
    serializer_class = OfferingSerializer


class AllBidMonitors(generics.ListAPIView):
    queryset = Offering.objects.all()
    serializer_class = OfferingSerializer


class AllBidPostAuction(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidAllocationSerializer


class CreateAllocation(generics.CreateAPIView):
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer


@api_view(['GET'])
def distribute_tokens(self):
    bids_list = []
    all_bids = list(Bid.objects.all().values())
    bids_list.append(all_bids)
    print(bids_list)

    # Bid.objects.annotate(bidding_price=Max(bidding_price)).filter(bidding_price=bidding_price).order_by('timestamp')
    query = Bid.objects.annotate(bid=Max('bidding_price')).order_by('-bidding_price')

    for item in range(len(query)):
        print(query[item].bidding_price)

    return Response(list(Bid.objects.annotate(bid=Count('bidding_price')).order_by('-bidding_price').values()))



