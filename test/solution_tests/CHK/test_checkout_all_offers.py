from solutions.CHK import checkout_solution
from solutions.CHK.prices_and_offers import prices, multi_offers, free_item_offers

class TestCheckoutAllOffers():
    def test_checkout_item_price(self):
        for item in prices:
            assert checkout_solution.checkout(item) == prices[item]
    
    def 