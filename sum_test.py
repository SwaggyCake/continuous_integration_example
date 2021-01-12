from sum import mysum
import pytest


@pytest.mark.parametrize('numbers, output', [
    ([1, 2.1, 3], 6.1),
    ([1, 2, 3, 4, 5], 15)
    # Ajoutez des tests pour que la somme des éléments de la liste soit égale à 10, 24 et 27
])
def test_mysum(numbers, output):
    assert mysum(numbers) == output
    for num in numbers:
        assert type(num) == int
    assert (len(numbers) % 2) == 1