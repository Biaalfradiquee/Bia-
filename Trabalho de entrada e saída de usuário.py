def imprimir_informacoes(nome, idade, cidade, sep=' | ', end='\n'):
    print("Nome:", nome, sep=sep, end=sep)
    print("Idade:", idade, sep=sep, end=sep)
    print("Cidade:", cidade, sep=sep, end=end)

# Exemplo de uso:
imprimir_informacoes("Beatriz", 21, "Rio de Janeiro")

def calcular():
    # Solicita ao usuário os números e a operação desejada
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    # Verifica a operação desejada e realiza o cálculo correspondente
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        # Verifica se o segundo número é zero para evitar divisão por zero
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero!")
            return
    else:
        print("Operação inválida!")
        return

    # Imprime o resultado da operação
    print("Resultado:", resultado)

# Exemplo de uso:
calcular()

def criar_lista_compras():
    # Solicita ao usuário que digite os itens da lista de compras separados por vírgula
    itens_input = input("Digite os itens da lista de compras, separados por vírgula: ")

    # Divide a entrada do usuário pela vírgula para obter os itens individuais
    itens = itens_input.split(',')

    # Imprime os itens em linhas separadas usando um laço
    print("Itens da lista de compras:")
    for item in itens:
        print(item.strip())  # strip() remove espaços em branco extras ao redor do item, se houver

# Exemplo de uso:
criar_lista_compras()

def converter_para_fahrenheit():
    # Solicita ao usuário a temperatura em graus Celsius
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converte a temperatura de Celsius para Fahrenheit
    fahrenheit = (celsius * 9/5) + 32

    # Imprime o resultado da conversão
    print("A temperatura em Fahrenheit é:", fahrenheit)

# Exemplo de uso:
converter_para_fahrenheit()

def solicitar_nomes():
    nomes = []  # Inicializa uma lista vazia para armazenar os nomes

    # Loop infinito para solicitar nomes até que 'sair' seja digitado
    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")

        if nome.lower() == 'sair':
            break  # Sai do loop se 'sair' for digitado
        else:
            nomes.append(nome)  # Adiciona o nome à lista de nomes

    # Imprime todos os nomes digitados, cada um em uma linha
    print("Nomes digitados:")
    for nome in nomes:
        print(nome)

# Exemplo de uso:
solicitar_nomes()