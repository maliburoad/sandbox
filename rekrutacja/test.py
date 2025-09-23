import pytest
from hypothesis import given, strategies as st

# Testowana funkcja — przykład: zlicza sumę
def sum_of_list(lst):
    return sum(lst)

# Test z użyciem Hypothesis i pytest
@given(st.permutations([1, 2, 3, 4, 5, 6, 7, 8]))
def test_sum_of_list_is_correct(permuted_list):
    # Dla celów demonstracyjnych wypisujemy permutację (normalnie nie robimy printów w testach)
    print("Testing with:", permuted_list)

    # Sprawdź, czy permutacja zawiera unikalne liczby od 1 do 8
    assert sorted(permuted_list) == list(range(1, 9))

    # Sprawdź czy suma jest równa znanej wartości (1+2+...+8 = 36)
    assert sum_of_list(permuted_list) == 36
