from django.db import models


class Bid(models.Model):
    user_id = models.IntegerField()
    bidding_price = models.FloatField()
    number_of_tokens = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Allocation(models.Model):
    bidding_object = models.ForeignKey(Bid, on_delete=models.CASCADE)
    number_of_token_received = models.IntegerField()

    def __str__(self):
        return str(self.bidding_object)


class BidMonitor(models.Model):
    total_number_of_token_available = models.IntegerField()
    bidding_window = models.DateTimeField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-id']
