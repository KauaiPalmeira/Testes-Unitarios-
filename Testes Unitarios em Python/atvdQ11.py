def somar_lista(lista):
    soma = 0
    for elemento in lista:
        if elemento >= 0:
            soma += elemento
    return soma

# Exemplo de uso:
lista_numeros = [1, -2, 3, 0, -4, 5, -6]
resultado = somar_lista(lista_numeros)
print(resultado)  # Deve imprimir 4 (1 + 3 + 0)
