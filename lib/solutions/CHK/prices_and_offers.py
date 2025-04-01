# !!! Caution when changing the prices !!!
# There is a edge case where applying the free item offers first
# then the multi-priced offer may yield a higher price for the customer.
# e.g. E = 40 B = 30 and if 2B for $1 and 2E for 1B free, for 'EEBB'
# 1. Apply free item offer first will yield: 40 + 40 + 30 = 110
# 2. Apply multi-priced offer first will yield: 40 + 40 + 1 = 81

prices = {
    'A': 50, 
    'B': 30, 
    'C': 20, 
    'D': 15, 
    'E': 40, 
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50
}

# Caution: Offer list must be in descending order of offer quantity
multi_offers = {
    'A': [(5, 200), (3, 130)], # 3A for 130, 5A for 200
    'B': [(2, 45)],  # 2B for 45   
    'H': [(10, 80), (5, 45)], # 5H for 45, 10H for 80
    'K': [(2, 150)], # 2K for 150
    'P': [(5, 200)], # 5P for 200
    'Q': [(3, 80)], # 3Q for 80
    'V': [(3, 130), (2, 90)], # 2V for 90, 3V for 130
}

free_item_offers = {
    'E': (2, 1, 'B'), # 2E for 1 free B
    'F': (2, 1, 'F'), # 2F for 1 free F
    'N': (3, 1, 'M'), # 3M for 1 free N
    'R': (3, 1, 'Q'), # 3R for 1 free Q
    'U': (3, 1, 'U'), # 3U for 1 free U

}

group_offers = [
    {
        'items': ['S', 'T', 'X', 'Y', 'Z'],
        'offer_qty': 3,
        'offer_price': 45
    }
]
