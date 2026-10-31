# VARIAVEIS

jogos = ['minecraft', 'roblox','valorant']

# GERENCIAMENTO

print ('=== GERENCIADOR DE JOGOS ===')

for posicao in range (len(jogos)):
    print (f'Posição: {posicao} - {jogos[posicao]}')
    
# DIGITAÇÃO DO USUÁRIO

jogo_digitado = input ('Digite o nome do jogo desejado: ').lower()

# VERIFICAÇÃO DO JOGO

if jogo_digitado in jogos:
    print ('Jogo encontrado!')
else:
    print ('Jogo não encontrado!')
    
# CADASTRO DE JOGOS

cadastrar = input ('Deseja cadastrar um novo jogo? (sim/não): ').lower()

if cadastrar == 'sim':
    novo_jogo = input ('Digite o nome do novo jogo: ').lower()
    
    if novo_jogo not in jogos:
       jogos.append (novo_jogo)
       print ('Jogo cadastrado com sucesso!')
    else:
       print ('Este jogo já está cadastrado!')
    
else:
    print ('Nenhum jogo foi adicionado.')

# REMOÇÃO

remover = input ('Deseja remover um jogo? (sim/não): ').lower()

if remover == 'sim':
    remover_jogo = input ('Qual jogo você deseja remover? ').lower()
    if remover_jogo in jogos:
       jogos.remove (remover_jogo)
       print ('Jogo removido com sucesso!')
    else:
       print ('Este jogo não está cadastrado!')

else:
    print ('Nenhum jogo foi removido.')

# RESULTADOS FINAIS
for posicao in range (len(jogos)):
    print (f'Posição: {posicao} - {jogos[posicao]}')
print (f'Total de jogos: {len(jogos)}')

# CONSULTA DA POSIÇÃO

posicao_desejada = int (input('Escolha a posição desejada:'))

if posicao_desejada >= 0 and posicao_desejada < len (jogos):
    print (f'Posição: {jogos[posicao_desejada]}')
else:
    print ('Posição inválida!')