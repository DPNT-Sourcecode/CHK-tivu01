

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    offers = {
        'A': [(5, 200), (3, 130)], # 3A for 130
        'B': [(2, 45)]   # 2B for 45   
    }

    free_item_offers = {
        'E': (2, 1, 'B'), # 2E for 1 free B
    }
    
    # !!! Caution when changing the prices !!!
    # There is a edge case where applying the free item offers first
    # then the multi-priced offer may yield a higher price for the customer.
    # e.g. E = 40 B = 30 and if 2B for $1 and 2E for 1B free, for 'EEBB'
    # 1. Apply free item offer first will yield: 40 + 40 + 30 = 110
    # 2. Apply multi-priced offer first will yield: 40 + 40 + 1 = 81


    # This implementation applies the free item offers first, then the 
    # multi-priced offers.

    counts = {}

    # Check for invalid inputs
    for sku in skus:
        if sku not in prices:
            return -1
        
        counts[sku] = counts.get(sku, 0) + 1
    
    # Apply free item offers
    for item, (offer_qty, free_qty, free_item) in free_item_offers.items():
        if item not in counts or free_item not in counts:
            continue

        num_free_offers = counts[item] // offer_qty
        counts[free_item] = max(0, counts[free_item] - num_free_offers * free_qty)

    total = 0

    # Calculate total price
    for item, count in counts.items():
        if item in offers:
            for offer_qty, offer_price in offers[item]:
                if count < offer_qty:
                    continue

                complete_offers = count // offer_qty
                total += complete_offers * offer_price
                count %= offer_qty # Update remaining item count
            total += count * prices[item]
        else:
            total += count * prices[item]

    return total
    
    


