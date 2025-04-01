from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_no_offer(self):
        assert checkout_solution.checkout('AA') == 100

    def test_checkout_with_offer(self):
        assert checkout_solution.checkout('AAA') == 130

    def test_checkout_multi_offer(self):
        assert checkout_solution.checkout('AAABB') == (130 + 45)

    def test_checkout_half_offer(self):
        assert checkout_solution.checkout('AAAA') == (130 + 50)

    def test_checkout_invalid(self):
        assert checkout_solution.checkout('AX') == -1

    def test_checkout_empty(self):
        assert checkout_solution.checkout('') == 0