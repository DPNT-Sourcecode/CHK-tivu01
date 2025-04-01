

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    offers = {
        'A': (3, 130), # 3A for 130
        'B': (2, 45)   # 2B for 45   
    }

    counts = {}

    # Check for invalid inputs
    for sku in skus:
        if sku not in prices:
            return -1
        
        counts[sku] = counts.get(sku, 0) + 1

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
    
    


