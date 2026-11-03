# VARIÁVEIS

jogos = ["minecraft", "valorant", "roblox"]
resposta = "sim"

# CONDIÇÕES

while resposta == 'sim':
    print ('\n=== MENU DE JOGOS ===')
    print ('1 - Mostrar jogos')
    print ('2 - Adicionar jogo')
    print ('3 - Remover jogo')
    print ('4 - Sair')

    #  OPÇÔES

    escolha = input ('Escolha uma opção: ')
    if escolha == '1':
        for jogo in jogos:
            print (f'Todos os jogos: {jogo}')

    elif escolha == '2':
     nome_jogo = input ('Qual o nome do jogo que você deseja adicionar: ').lower()

     if nome_jogo not in jogos:
         jogos.append (nome_jogo)
         print ('Jogo adicionado com sucesso!')
     else:
         print ('Jogo já cadastrado')

    elif escolha == '3':
        remover_jogo = input ('Qual o nome do jogo que você deseja remover? ').lower()
        if remover_jogo in jogos:
            jogos.remove (remover_jogo)
            print('Jogo removido com sucesso!')
        else:
            print ('Jogo não encontrado!')
    elif escolha == '4':
     resposta = 'não'

    else:
         print('Opção inválida!')

print ('Programa encerrado!')