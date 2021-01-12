from sum import mysum


def test_sum_integers():
    assert mysum([0, 1, 2, 3, 4]) == 10
def test_sum_floats():
    assert mysum([0.1, 1.2, 2.3, 3.4, 4.5]) == 11.5
def test_sum_nothing():
    assert mysum([]) == 0
def test_type_sum_integers():
    assert type(mysum([0, 1, 2, 3, 4])) == int

def test_type_sum():
    assert mysum([0, 1, 2, 3, 4]) > 0


