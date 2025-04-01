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

    # Free item offer tests
    def test_checkout_free_item_offer(self):
        assert checkout_solution.checkout('EEB') == 80

    def test_checkout_free_item_offer2(self):
        assert checkout_solution.checkout('EEBB') == (80 + 30)

    def test_checkout_multiple_free_item_offer(self):
        assert checkout_solution.checkout('EEEEBB') == (80 + 80)

    def test_checkout_no_free_item_offer(self):
        assert checkout_solution.checkout('EB') == 70

    # Free item offer same item tests
    def test_checkout_free_item_offer_same_item(self):
        assert checkout_solution.checkout('FFF') == 20

    def test_checkout_free_item_offer2_same_item(self):
        assert checkout_solution.checkout('FFFFFF') == (20 * 2)

    def test_checkout_multiple_free_item_offer_same_item(self):
        assert checkout_solution.checkout('FFFFFFF') == (20 * 2 + 10)

    def test_checkout_no_free_item_offer_same_item(self):
        assert checkout_solution.checkout('FF') == 20

    # Multiple multi-priced offer tests
    def test_checkout_best_multi_offer(self):
        assert checkout_solution.checkout('AAAAA') == 200

    def test_checkout_multiple_multi_offer(self):
        assert checkout_solution.checkout('AAAAAAAA') == (200 + 130)

    def test_checkout_multiple_multi_offer_and_remaining(self):
        assert checkout_solution.checkout('AAAAAAAAA') == (200 + 130 + 50)