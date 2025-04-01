from prices_and_offers import prices, multi_offers, free_item_offers

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
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
        if item == free_item:
            # Ensure number of self free item is sufficient
            num_free_offers = counts[item] // (offer_qty + free_qty) 
        else:
            num_free_offers = counts[item] // offer_qty
        counts[free_item] = max(0, counts[free_item] - num_free_offers * free_qty)

    total = 0

    # Calculate total price
    for item, count in counts.items():
        if item in multi_offers:
            for offer_qty, offer_price in multi_offers[item]:
                if count < offer_qty:
                    continue

                complete_offers = count // offer_qty
                total += complete_offers * offer_price
                count %= offer_qty # Update remaining item count
            total += count * prices[item]
        else:
            total += count * prices[item]

    return total
    
    


