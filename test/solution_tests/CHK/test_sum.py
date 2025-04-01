from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_no_offer(self):
        assert checkout_solution.checkout('AA') == 100
