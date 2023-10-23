import unittest

# Função que calcula a média de uma lista de números
def calcular_média(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    return sum(lista) / len(lista)

# Classe de teste para a função calcular_média
class TestCalcularMédia(unittest.TestCase):

    def testarLista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_média([])

    def testarLista_com_um_elemento(self):
        self.assertEqual(calcular_média([42]), 42.0)

    def testarLista_com_elementos_positivos(self):
        self.assertEqual(calcular_média([1, 2, 3, 4, 5]), 3.0)

    def testarLista_com_elementos_negativos(self):
        self.assertEqual(calcular_média([-1, -2, -3, -4, -5]), -3.0)

    def testarLista_com_elementos_mistos(self):
        self.assertEqual(calcular_média([1, -2, 3, -4, 5]), 0.6)

if __name__ == '__main__':
    unittest.main()
