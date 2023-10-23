import unittest

# Função que verifica se um número é par
def é_par(numero):
    return numero % 2 == 0

# Classe de teste para a função é_par
class TestÉPar(unittest.TestCase):

    def testar_numero_par(self):
        self.assertTrue(é_par(2))
        self.assertTrue(é_par(4))
        self.assertTrue(é_par(100))
        self.assertTrue(é_par(-6))

    def testar_numero_impar(self):
        self.assertFalse(é_par(3))
        self.assertFalse(é_par(7))
        self.assertFalse(é_par(11))
        self.assertFalse(é_par(-5))

if __name__ == '__main__':
    unittest.main()
