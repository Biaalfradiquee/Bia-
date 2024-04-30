print("Olá", "mundo", sep="-") # Saída: Olá-mundo
print("Olá", "Python", end="!\n") # Saída: Olá Python!

# Saída: 18/04/2023 (formato de data)
print("18", "04", "2023", sep="/")
# Saída: nome; sobrenome; email (útil em CSVs)
print("nome", "sobrenome", "email", sep="; ") 

# Continuando impressões na mesma linha
print("Loading", end=" ")
print("[OK]") # Saída: Loading [OK]

#nome = input("Digite seu nome: ")
#print("Olá", nome)

# Captura uma linha de entrada e a converte em uma lista de strings
#itens = input("Digite itens separados por vírgula: ")

#ites = itens.split(',')

#print("Itens:", itens)

# Convertendo a entrada para inteiro
#idade = int(input("Digite sua idade: "))
#print("Daqui a cinco anos, você terá", idade + 5, "anos.")

# Convertendo a entrada para float
#altura = float(input("Digite sua altura em metros: "))
#print("Sua altura é", altura, "metros.")

def infinito():
    print("Digite números para adicionar à lista (digite 'done' para terminar):")
    numeros = []
    while True:
        entrada = input()
        if entrada.lower() == 'done':
            break
        else:
            numeros.append(int(entrada))
    print("Números coletados:", numeros)




