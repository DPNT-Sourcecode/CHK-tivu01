

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    offers = {
        'A': (3, 130), # 3A for 130
        'B': (2, 45)   # 2B for 45   
    }

    free_item_offers = {
        'E': (2, 1, 'B'), # 2E for 1 free B
    }

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
            offer_qty, offer_price = offers[item]
            complete_offers = count // offer_qty
            remaining_items = count % offer_qty
            total += complete_offers * offer_price + remaining_items * prices[item]
        else:
            total += count * prices[item]

    return total
    
    



