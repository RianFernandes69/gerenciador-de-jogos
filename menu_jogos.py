# VARIÁVEIS

jogos = ["minecraft", "valorant", "roblox"]
resposta = "sim"

# CONDIÇÕES

while resposta == 'sim':
    print ('\n=== MENU DE JOGOS ===')
    print ('1 - Mostrar jogos')
    print ('2 - Sair')

    #  OPÇÔES

    escolha = input ('Escolha uma opção: ')
    if escolha == 1:
        for escolha in jogos: