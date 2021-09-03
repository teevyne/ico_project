import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_bid_tokens(value):
    if value <= 0:
        raise ValidationError(
            _('%(value)s is not valid'),
            params={'value': value},
        )


class Offering(models.Model):
    total_number_of_token_available = models.IntegerField()
    bidding_window_open = models.DateTimeField()
    bidding_window_closed = models.DateTimeField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-id']

    def clean(self):
        # Don't allow the open window be greater than close window
        if self.bidding_window_open >= self.bidding_window_closed:
            raise ValidationError(_(
                "The offering opening date must not be greater than the closing date"))


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    def __str__(self):
        return self.username


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bidding_price = models.FloatField(validators=[validate_bid_tokens])
    number_of_tokens = models.IntegerField(validators=[validate_bid_tokens])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Allocation(models.Model):
    bid = models.OneToOneField(Bid, on_delete=models.CASCADE, related_name='bid_object')
    number_of_token_received = models.IntegerField()

    def __str__(self):
        return str(self.bid)
