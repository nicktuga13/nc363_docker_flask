import calculator.operations


def test_calculator_add_method():
    assert calculator.operations.Addition.add(1, 1) == 2


def test_calculator_sub_method():
    assert calculator.operations.Subtract.subtract(1, 1) == 0


def test_calculator_mult_method():
    assert calculator.operations.Multiply.multiply(1, 1) == 1

