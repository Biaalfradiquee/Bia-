def calcular_soma_e_media(numeros):
    """
    Esta função recebe uma lista de números e retorna a soma e a média dos números.
    """
    soma_dos_numeros = sum(numeros)
    media_dos_numeros = soma_dos_numeros / len(numeros) if numeros else 0
    return soma_dos_numeros, media_dos_numeros

def substituir_palavra_na_lista(lista_de_palavras, palavra_antiga, nova_palavra):
    """
    Esta função recebe uma lista de palavras, uma palavra a ser substituída, e a nova palavra.
    Retorna uma nova lista com as ocorrências da palavra antiga substituídas pela nova palavra.
    """
    return [nova_palavra if palavra == palavra_antiga else palavra for palavra in lista_de_palavras]

def imprimir_triangulo_de_asteriscos(linhas):
    """
    Esta função recebe um número de linhas e imprime um triângulo de asteriscos com esse número de linhas.
    """
    for i in range(1, linhas + 1):
        print('*' * i)

# Testando as funções
print(calcular_soma_e_media([1, 2, 3, 4, 5, 6]))  # Saída: (10, 2.5)
print(substituir_palavra_na_lista(["banana", "morango", "limão"], "morango", "laranja"))  # Saída: ['banana', 'uva', 'limão']

imprimir_triangulo_de_asteriscos(9)

    