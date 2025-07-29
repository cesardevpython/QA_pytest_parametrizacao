import pytest
from codigo.calculos import eh_par, dividir

@pytest.mark.parametrize("a, b, esperado", [
    (20, 4, 5),
    (15, 3, 5),
    (9, 3, 3)
])
def test_dividir_parametrizado(a, b, esperado):
    assert dividir(a, b) == esperado

@pytest.mark.parametrize("numero, esperado", [
    (4, True),
    (5, False),
    (0, True),
    (7, False)
])
def test_eh_par_parametrizado(numero, esperado):
    assert eh_par(numero) == esperado