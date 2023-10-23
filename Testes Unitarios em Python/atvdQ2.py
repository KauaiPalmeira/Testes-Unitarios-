import unittest

# Função que calcula o fatorial de um número inteiro não negativo
def fatorial(n):
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Classe de teste para a função fatorial
class TestFatorial(unittest.TestCase):

    def test_fatorial_numero_zero(self):
        self.assertEqual(fatorial(0), 1)

    def test_fatorial_numeros_p(self):
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(2), 2)
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(10), 362880)

    def test_fatorial_numero_n(self):
        with self.assertRaises(ValueError):
            fatorial(-5)

if __name__ == '__main__':
    unittest.main()
