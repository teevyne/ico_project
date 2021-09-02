from django.urls import path

from icoapp.views import (
    CreateBid,
    DetailBid,
    AllBids,
    CreateMonitor,
    DetailMonitor,
    AllBidMonitors, AllBidPostAuction, CreateAllocation
)

urlpatterns = [
    path('create-bid', CreateBid.as_view()),
    path('get-bid/<int:pk>', DetailBid.as_view()),
    path('get-all-bids', AllBids.as_view()),

    path('get-all-bid-monitors', AllBidMonitors.as_view()),
    path('create-bid-monitor', CreateMonitor.as_view()),
    path('get-bid-monitor/<int:pk>', DetailMonitor.as_view()),

    path('all-bids-post-auction/', AllBidPostAuction.as_view()),

    path('create-allocation', CreateAllocation.as_view()),
]
