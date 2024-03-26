def calcular_soma_e_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

def substituir_palavra(lista, palavra_procurada, nova_palavra):
    nova_lista = [nova_palavra if palavra == palavra_procurada else palavra for palavra in lista]
    return nova_lista

def imprimir_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)

# Testando as funções
if __name__ == "__main__":
    lista_numeros = [1, 2, 3, 4]
    soma, media = calcular_soma_e_media(lista_numeros)
    print("Soma:", soma)
    print("Média:", media)

    lista_palavras = ["banana", "morango", "limão"]
    palavra_procurada = "morango"
    nova_palavra = "maçã"
    nova_lista = substituir_palavra(lista_palavras, palavra_procurada, nova_palavra)
    print("Lista alterada:", nova_lista)

    num_linhas = 4
    imprimir_triangulo(num_linhas)

