from django.urls import path

from icoapp.views import CreateBid, DetailBid, AllBids, CreateMonitor, DetailMonitor

urlpatterns = [
    path('create-bid', CreateBid.as_view()),
    path('get-bid/<int:pk>', DetailBid.as_view()),
    path('get-all-bids', AllBids.as_view()),

    path('create-bid-monitor', CreateMonitor.as_view()),
    path('update-monitor/<int:pk>', DetailMonitor.as_view()),

]