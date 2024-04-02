def soma_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

def substituir_palavra(lista, palavra_antiga, palavra_nova):
    return [palavra_nova if palavra == palavra_antiga else palavra for palavra in lista]

def imprimir_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)

# Exemplos de uso das funções:
lista_numeros = [1, 2, 3, 4]
soma, media = soma_media(lista_numeros)
print("Soma:", soma)
print("Média:", media)

lista_palavras = ["banana", "morango", "limão"]
nova_lista = substituir_palavra(lista_palavras, "morango", "maçã")
print("Lista com palavra substituída:", nova_lista)

imprimir_triangulo(4)
