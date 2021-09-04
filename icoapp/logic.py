from functools import reduce
from icoapp.models import Offering, Bid

available = Offering.objects.first().total_number_of_token_available
price_group = []
current_bid_index = 0

while available > 0:
    current_bid = query[current_bid_index]

    while (check := query[current_bid]).price == current_bid.price:
        price_group.append(check)

    # at this point we have items of the same price. We can start allocating

    # let's get the number of tokens they'll all need together.

    total_tokens = reduce(
        lambda first, second: first.tokens + second.tokens if isinstance(first, Bid) else first + second.tokens)

    # now we have total number of tokens needed. We then need to check if we can give them all they want or we can't

    if available - total_tokens < 0:
        total_tokens = available

    # now we can share tokens