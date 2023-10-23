import unittest

# Classe ContaBancária que realiza operações de depósito e saque
class ContaBancária:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor < 0:
            raise ValueError("O valor do depósito não pode ser negativo.")
        self.saldo += valor

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("O valor do saque não pode ser negativo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para o saque.")
        self.saldo -= valor

# Classe de teste para a classe ContaBancária
class TestContaBancária(unittest.TestCase):

    def setUp(self):
        self.conta = ContaBancária(1000)

    def test_depositar(self):
        self.conta.depositar(500)
        self.assertEqual(self.conta.saldo, 1500)

    def test_sacar(self):
        self.conta.sacar(300)
        self.assertEqual(self.conta.saldo, 700)

    def test_saldo_insuficiente(self):
        with self.assertRaises(ValueError):
            self.conta.sacar(1200)

    def testar_deposito_n(self):
        with self.assertRaises(ValueError):
            self.conta.depositar(-200)

    def testar_saque_n(self):
        with self.assertRaises(ValueError):
            self.conta.sacar(-300)

if __name__ == '__main__':
    unittest.main()
