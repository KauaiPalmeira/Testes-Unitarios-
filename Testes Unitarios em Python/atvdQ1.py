import unittest

# Função que realiza a soma de dois números
def soma(a, b):
    return a + b

# Classe de teste para a função soma
class TestSoma(unittest.TestCase):

    def testarSoma_numero_p(self):
        self.assertEqual(soma(5,3),8)
        self.assertEqual(soma(3,2),5)
        self.assertEqual(soma(5,5), 10)
        self.assertEqual(soma(20,20),40)
    def testar_soma_numeros_n(self):
        self.assertEqual(soma(-3, -5), -8)  # -3 + (-5) = -8
        self.assertEqual(soma(-10, 5), -5)  # -10 + 5 = -5
        self.assertEqual(soma(0, -5), -5)   # 0 + (-5) = -5

if __name__ == '__main__':
    unittest.main()
