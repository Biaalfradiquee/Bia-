def gravar_nome_em_arquivo():
    # Solicita que o usuário informe seu nome
    nome = input("Por favor, informe seu nome: ")

    # Abre o arquivo em modo de escrita ('w'), cria o arquivo se não existir
    with open("nome.txt", "w") as arquivo:
        # Escreve o nome fornecido pelo usuário no arquivo
        arquivo.write(nome)

    print("Nome gravado com sucesso no arquivo 'nome.txt'.")

# Chamada da função para executá-la
gravar_nome_em_arquivo()

def imprimir_conteudo_arquivo():
    # Solicita que o usuário informe o nome do arquivo
    nome_arquivo = input("Por favor, informe o nome do arquivo de texto: ")

    # Abre o arquivo em modo de leitura ('r')
    with open(nome_arquivo, "r") as arquivo:
        # Lê todo o conteúdo do arquivo
        conteudo = arquivo.read()

    # Imprime o conteúdo do arquivo
    print("Conteúdo do arquivo {}:\n".format(nome_arquivo))
    print(conteudo)

# Chamada da função para executá-la
imprimir_conteudo_arquivo()

def copiar_conteudo_arquivo(nome_arquivo_origem, nome_arquivo_destino):
    # Abre o arquivo de origem em modo de leitura ('r')
    with open(nome_arquivo_origem, "r") as arquivo_origem:
        # Lê todo o conteúdo do arquivo de origem
        conteudo = arquivo_origem.read()

    # Abre o arquivo de destino em modo de escrita ('w'), cria o arquivo se não existir
    with open(nome_arquivo_destino, "w") as arquivo_destino:
        # Escreve o conteúdo lido do arquivo de origem no arquivo de destino
        arquivo_destino.write(conteudo)

    print("Conteúdo do arquivo '{}' copiado com sucesso para '{}'.".format(nome_arquivo_origem, nome_arquivo_destino))

# Exemplo de utilização da função
arquivo_origem = "arquivo_origem.txt"  # Nome do arquivo de origem
arquivo_destino = "arquivo_destino.txt"  # Nome do arquivo de destino

# Chamada da função para copiar o conteúdo do arquivo de origem para o arquivo de destino
copiar_conteudo_arquivo(arquivo_origem, arquivo_destino)

def encontrar_nome_por_numero(numero_procurado):
    # Abre o arquivo em modo de leitura ('r')
    with open("arquivo_exemplo.txt", "r") as arquivo:
        # Lê as linhas do arquivo
        linhas = arquivo.readlines()

        # Percorre cada linha do arquivo
        for linha in linhas:
            # Divide a linha em partes separadas por espaços em branco
            partes = linha.split()

            # Se o primeiro elemento da linha (o número) for igual ao número procurado
            if partes[0] == str(numero_procurado):
                # O nome correspondente está no segundo elemento da linha
                nome_correspondente = partes[1]
                # Imprime o nome correspondente
                print("O nome correspondente ao número {} é: {}".format(numero_procurado, nome_correspondente))
                # Retorna para encerrar a função após encontrar o nome
                return

    # Se o número não foi encontrado no arquivo
    print("Número não encontrado no arquivo.")

# Solicita ao usuário que informe um número
numero_usuario = int(input("Por favor, informe um número: "))

# Chamada da função para encontrar o nome correspondente ao número informado pelo usuário
encontrar_nome_por_numero(numero_usuario)