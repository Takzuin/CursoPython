def sumar(a, b):
    return a + b

def test_suma_simple():
    assert sumar(2, 3) == 5

def test_suma_negativos():
    assert sumar(-1, -1) == -2
