import unittest

# Função que ordena uma lista de números em ordem crescente
def ordenar_lista(lista):
    return sorted(lista)

# Classe de teste para a função ordenar_lista
class TestOrdenarLista(unittest.TestCase):

    def testarLista_vazia(self):
        self.assertEqual(ordenar_lista([]), [])

    def testarLista_com_um_elemento(self):
        self.assertEqual(ordenar_lista([42]), [42])

    def testarLista_com_elementos_em_ordem_crescente(self):
        self.assertEqual(ordenar_lista([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def testarLista_com_elementos_em_ordem_decrescente(self):
        self.assertEqual(ordenar_lista([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def testarLista_com_elementos_desordenados(self):
        self.assertEqual(ordenar_lista([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

if __name__ == '__main__':
    unittest.main()
