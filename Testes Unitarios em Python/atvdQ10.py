import unittest

# Função que inverte uma string
def inverter_string(string):
    return string[::-1]

# Classe de teste para a função inverter_string
class TestInverterString(unittest.TestCase):

    def testarString_vazia(self):
        self.assertEqual(inverter_string(""), "")

    def testarString_com_um_caractere(self):
        self.assertEqual(inverter_string("a"), "a")

    def testarString_com_varios_caracteres(self):
        self.assertEqual(inverter_string("oi"), "io")
        self.assertEqual(inverter_string("Python"), "nohtyP")
        self.assertEqual(inverter_string("1010"), "0101")

if __name__ == '__main__':
    unittest.main()
