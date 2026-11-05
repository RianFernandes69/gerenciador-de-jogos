# VARIAVEIS

jogos = ['minecraft', 'roblox','valorant']
resposta = 'sim'

# FUNÇÕES

def mostrar_jogos():
    for posicao in range(len(jogos)):
        print(f'Posição: {posicao} - {jogos[posicao]}')
all
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

# MENU

while resposta == 'sim':
    print ('1 - Mostrar jogos')
    print ('2 - Pesquisar jogo')
    print ('3 - Cadastrar jogo')
    print ('4 - Consultar posição')
    print ('5 - Remover jogo')
    print ('6 - Sair')

    # OPÇÕES

    escolha = input ('Escolha uma das opções: ')
    if escolha == '6':
        resposta = 'não'

    elif escolha == '1':
        print('\n=== MINHA LISTA DE JOGOS ===')
        mostrar_jogos()

    # BUSCA DO JOGO

    elif escolha == '2':
       pesquisa = input ('Qual o jogo que você está buscando? ').lower()
       print(pesquisa_jogo(pesquisa))
    # ADICIONANDO O JOGO

    elif escolha == '3':
       adicionar = input ('Escolha o jogo que você deseja adicionar: ').lower()
       print(adicionar_jogo(adicionar))

    # CONSULTANDO A POSIÇÃO

    elif escolha == "4":
      consulta = int (input ('Qual posição você deseja consultar? '))
      consultar_posicao(consulta)

    # REMOÇÃO DO JOGO

    elif escolha == '5':
       remocao = input ('Qual o jogo que você deseja remover? ').lower()
       print (remover_jogo(remocao))

    else:
        print ("Opção inválida!")

print ('Programa encerrado!')

 # FINAL DA REPETIÇÃO

print ('\n=== RESULTADOS FINAIS ===')
mostrar_jogos ()
print (f"Total de jogos: {contar_jogos(jogos)}")

all
