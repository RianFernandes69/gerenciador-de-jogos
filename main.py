# VARIAVEIS

jogos = ['minecraft', 'roblox','valorant']
resposta = 'sim'

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
       print ('\n=== MINHA LISTA DE JOGOS ===')
       for posicao in range(len(jogos)):
          print (f'Posição: {posicao} - {jogos [posicao]}')

    # BUSCA DO JOGO

    elif escolha == '2':
       pesquisa = input ('Qual o jogo que você está buscando? ').lower()
       if pesquisa in jogos:
          print ('Jogo encontrado!')
       else:
          print ('Jogo não encontrado!')

    # ADICIONANDO O JOGO      

    elif escolha == '3':
       adicionar = input ('Escolha o jogo que você deseja adicionar: ').lower()
       if adicionar not in jogos:
          jogos.append (adicionar)
          print ('Jogo adicionado com sucesso!')
       else:
          print ('O jogo já está na lista!')

    # CONSULTANDO A POSIÇÃO

    elif escolha == "4":
      consulta = int (input ('Qual posição você deseja consultar? '))
      if consulta >= 0 and consulta < len (jogos):
         print (f'Posição {consulta} - {jogos [consulta]}')
      else:
         print ('Posição não encontrada')

    # REMOÇÃO DO JOGO

    elif escolha == '5':
       remocao = input ('Qual o jogo que você deseja remover? ').lower()
       if remocao in jogos:
          jogos.remove (remocao)
          print ('Jogo removido com sucesso!')
       else:
          print ('Jogo não encontrado!')
    else:
     print ('Opção inválida!')
print ('Programa encerrado!')

 # FINAL DA REPETIÇÃO

print ('=== RESULTADOS FINAIS ===')
for posicao in range(len(jogos)):
    print(f'Posição: {posicao} - {jogos[posicao]}')
print(f'Total de jogos: {len(jogos)}')
    
