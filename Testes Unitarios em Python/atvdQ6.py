import unittest

# Função que conta o número de vogais em uma string
def contar_vogais(string):
    vogais = "AEIOUaeiou"
    contador = 0
    for char in string:
        if char in vogais:
            contador += 1
    return contador

# Classe de teste para a função contar_vogais
class TestContarVogais(unittest.TestCase):

    def testString_sem_vogais(self):
        self.assertEqual(contar_vogais("Rhythm"), 0)

    def testarString_com_vogais(self):
        self.assertEqual(contar_vogais("Hello World"), 3)
        self.assertEqual(contar_vogais("OpenAI"), 4)
        self.assertEqual(contar_vogais("Python"), 1)
        self.assertEqual(contar_vogais("AEIOUaeiou"), 10)

    def test_string_vazia(self):
        self.assertEqual(contar_vogais(""), 0)

if __name__ == '__main__':
    unittest.main()
