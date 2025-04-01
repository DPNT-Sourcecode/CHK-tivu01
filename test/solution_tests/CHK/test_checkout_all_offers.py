from solutions.CHK import checkout_solution
from solutions.CHK.prices_and_offers import prices, multi_offers, free_item_offers, group_offers

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
        pass

