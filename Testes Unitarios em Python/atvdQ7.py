import unittest

# Função que verifica se um número é primo
def é_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Classe de teste para a função é_primo
class TestÉPrimo(unittest.TestCase):

    def test_primos(self):
        self.assertTrue(é_primo(2))
        self.assertTrue(é_primo(3))
        self.assertTrue(é_primo(5))
        self.assertTrue(é_primo(7))
        self.assertTrue(é_primo(11))
        self.assertTrue(é_primo(13))
        self.assertTrue(é_primo(17))
        self.assertTrue(é_primo(19))

    def test_nao_primos(self):
        self.assertFalse(é_primo(0))
        self.assertFalse(é_primo(1))
        self.assertFalse(é_primo(4))
        self.assertFalse(é_primo(6))
        self.assertFalse(é_primo(8))
        self.assertFalse(é_primo(9))
        self.assertFalse(é_primo(15))
        self.assertFalse(é_primo(21))

if __name__ == '__main__':
    unittest.main()
