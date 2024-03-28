import calculator


class TestCalculator:
    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_subtract(self):
        assert 4 == calculator.subtract(6, 2)

    def test_multiply(self):
        assert 4 == calculator.mul(2, 2)
