from functools import reduce
from icoapp.models import Bid, Offering

all_bids = list(Bid.objects.all().values())
query = sorted(all_bids, key=lambda bid: (bid['bidding_price'], bid['timestamp']), reverse=True)

available = Offering.objects.first().total_number_of_token_available
price_group = []
current_bid_index = 0
all_bids = []

while available > 0 and current_bid_index < len(query):
    current_bid = query[current_bid_index]

    while current_bid_index < len(query) and (check := query[current_bid_index]).price == current_bid.price:
        price_group.append(check)
        current_bid_index += 1

    total_tokens = reduce(
        lambda first, second: first.number_of_tokens + second.tokens if isinstance(
            first,
            Bid
        ) else first + second.tokens, price_group,
        0
    )

    if available - total_tokens > 0:
        for card in price_group:
            card.received = card.tokens

        available -= total_tokens
        all_bids.extend(price_group)
        total_tokens = 0
        price_group = []
    else:
        total_tokens = available

    available -= total_tokens
    current_sub_bid = 0

    while total_tokens > 0 and price_group:
        price_group[current_sub_bid].received += 1

        if (current := price_group[current_sub_bid]).received == current.tokens:
            all_bids.append(current)
            price_group.pop(current_sub_bid)

        total_tokens -= 1

        if total_tokens == 0:
            all_bids.extend(price_group)

        if current_sub_bid >= len(price_group) - 1:
            current_sub_bid = 0
        else:
            current_sub_bid += 1

# for all_bids
for card in all_bids:
    print(card)

# uncomment below to see who was satisfied and who wasn't.
satisfied = list(filter(lambda card: card.received, all_bids))
unsatisfied = list(filter(lambda card: not card.received, all_bids))