# VARIÁVEIS

jogos = ["minecraft", "valorant", "roblox"]

# FUNÇÕES

def mostrar_jogos():
    for jogo in jogos:
        print (f'Jogo: {jogo}')

# FUNÇÃO PARA PESQUISA

def pesquisa_jogo(nome):
    if nome in jogos:
        return 'Jogo encontrado!'
    else:
        return 'Jogo não encontrado!'

# FUNÇÃO PARA ADIÇÃO

def adicionar_jogo(nome):
    if nome not in jogos:
        jogos.append(nome)
        return 'Jogo adicionado com sucesso!'
    else:
        return 'Jogo já cadastrado!'

# FUNÇÃO PARA REMOVER

def remover_jogo(nome):
    if nome in jogos:
        jogos.remove(nome)
        return 'Jogo removido com sucesso!'
    else:
        return 'Jogo não encontrado'

# FUNÇÃO PARA CONSULTA

def consultar_posicao(posicao):
    if posicao >= 0 and posicao < len (jogos):
        print (f'Posição: {posicao} - {jogos [posicao]}')
    else:
        print ('Posição inválida!')

# FUNÇÃO PARA CONTAR JOGOOS

def contar_jogos(lista):
    return len(lista)

# MENU PRINCIPAL

opcao = ''

while opcao != '7':
    print("\n=== GERENCIADOR DE JOGOS ===")
    print("1 - Mostrar jogos")
    print("2 - Adicionar jogo")
    print("3 - Remover jogo")
    print("4 - Pesquisar jogo")
    print("5 - Consultar posição")
    print("6 - Contar jogos")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        mostrar_jogos()

    elif opcao == '2':
        nome_jogo = input ('Qual o nome do jogo que você deseja adicionar? ').lower()
        print (adicionar_jogo (nome_jogo))



    elif opcao == "3":
        nome_jogo = input ("Qual jogo você deseja remover? ").lower()
        print (remover_jogo (nome_jogo))

    elif opcao == "4":
        nome_jogo = input ("Qual o jogo que você está buscando? ").lower()
        print (pesquisa_jogo (nome_jogo))

    elif opcao == "5":
        posicao_desejada = int (input ("Escolha uma posição: "))
        consultar_posicao(posicao_desejada)

    elif opcao == "6":
        print (f"Total de jogos: {contar_jogos(jogos)}")

    elif opcao == "7":
        print ("Obrigado por testar o programa.\nAté a próxima!")

    else:
        print ("Opção inválida!")

# ENCERRAMENTO DO PROGRAMA

print ("Programa encerrado!")