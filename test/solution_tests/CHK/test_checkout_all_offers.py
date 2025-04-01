from solutions.CHK import checkout_solution
from solutions.CHK.prices_and_offers import prices, multi_offers, free_item_offers, group_offers
import random

class TestCheckoutAllOffers():
    def test_checkout_item_price(self):
        for item in prices:
            assert checkout_solution.checkout(item) == prices[item]
    
    def test_checkout_multi_offers(self):
        for item, offers in multi_offers.items():

            # Apply single multi-priced offer
            for offer_qty, offer_price in offers:
                assert checkout_solution.checkout(item * offer_qty) == offer_price 

            skus = ''
            total_offer_price = 0
            # Apply multiple multi-priced offer
            for offer_qty, offer_price in offers:
                skus += item * offer_qty
                total_offer_price += offer_price
                
            assert checkout_solution.checkout(skus) == total_offer_price

    def test_checkout_free_item_offers(self):
        for item, (offer_qty, free_qty, free_item) in free_item_offers.items():
            assert checkout_solution.checkout(item * offer_qty + free_item * free_qty) == prices[item] * offer_qty

    def test_checkout_group_offers(self):
        for offer in group_offers:
            group_items = offer['items']
            offer_qty = offer['offer_qty']
            offer_price = offer['offer_price']

            group_items.sort(key= lambda x: prices[x], reverse=True)

            # Apply single group offer
            skus = ''
            for i in range(offer_qty):
                skus += group_items[i]

            assert checkout_solution.checkout(skus) == offer_price

            # Apply single group offer with extras
            skus = ''
            for i in range(offer_qty + 1):
                skus += group_items[i]
            
            l = list(skus)
            random.shuffle(l)
            skus = ''.join(l)
            assert checkout_solution.checkout(skus) == offer_price + prices[group_items[i]]



        pass


