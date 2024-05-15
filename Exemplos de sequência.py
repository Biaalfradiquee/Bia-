def bombom(dinheiro, preco):
    numero_bombons = dinheiro // preco  # Calcula o número de bombons que podem ser comprados
    troco = dinheiro % preco  # Calcula o troco
    return numero_bombons, troco  # Retorna uma tupla com o número de bombons e o troco

# Exemplo de uso da função
dinheiro_de_joaozinho = 2540
preco_do_bombom = 25

numero_bombons, troco = bombom(dinheiro_de_joaozinho, preco_do_bombom)
print(f"Joãozinho pode comprar {numero_bombons} bombons e sobrarão R${troco} de troco.")

def bombom(dinheiro, preco):
    numero_bombons = dinheiro // preco  # Calcula o número de bombons que podem ser comprados
    troco = dinheiro % preco  # Calcula o troco
    return numero_bombons, troco  # Retorna uma tupla com o número de bombons e o troco

def maisbombom(dinheiro, preco):
    troco_atual = bombom(dinheiro, preco)[1]
    dinheiro_necessario = preco - troco_atual
    return dinheiro_necessario

# Teste das funções
dinheiro_de_joaozinho = 2540
preco_do_bombom = 25

numero_bombons, troco = bombom(dinheiro_de_joaozinho, preco_do_bombom)
dinheiro_a_pedir = maisbombom(dinheiro_de_joaozinho, preco_do_bombom)

print(f"Joãozinho pode comprar {numero_bombons} bombons e sobrarão R${troco} de troco.")
print(f"Joãozinho precisa pedir mais R${dinheiro_a_pedir} para comprar outro bombom.")

def bombom(dinheiro, preco):
    numero_bombons = dinheiro // preco  # Calcula o número de bombons que podem ser comprados
    troco = dinheiro % preco  # Calcula o troco
    return numero_bombons, troco  # Retorna uma tupla com o número de bombons e o troco

def maisbombom(dinheiro, preco):
    troco_atual = bombom(dinheiro, preco)[1]
    dinheiro_necessario = preco - troco_atual
    return dinheiro_necessario

# Teste das funções
dinheiro_de_joaozinho = 2540
preco_do_bombom = 25

numero_bombons, troco = bombom(dinheiro_de_joaozinho, preco_do_bombom)
dinheiro_a_pedir = maisbombom(dinheiro_de_joaozinho, preco_do_bombom)

print(f"Joãozinho pode comprar {numero_bombons} bombons e sobrarão R${troco} de troco.")
print(f"Joãozinho precisa pedir mais R${dinheiro_a_pedir} para comprar outro bombom.")

def listar_pares(n):
    """ Retorna uma lista contendo todos os números pares entre 1 e n, inclusive. """
    return list(range(2, n+1, 2))

# Exemplo de uso da função
resultado = listar_pares(50)
print("Números pares entre 1 e 50:", resultado)