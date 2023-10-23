import unittest

# Classe Calculadora que realiza operações matemáticas
class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b

# Classe de teste para a classe Calculadora
class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calc.somar(3, 5), 8)

    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(10, 7), 3)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(4, 6), 24)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(15, 3), 5)
        self.assertAlmostEqual(self.calc.dividir(7, 2), 3.5, places=2)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()
