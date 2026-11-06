# IMPORTAÇÃO

from gerenciador_v4 import (

    pesquisa_jogo, 
    adicionar_jogo,
    remover_jogo, 
    consultar_posicao,
    contar_jogos,
    mostrar_jogos,
    jogos

)

# TESTE DE PESQUISA
print("TESTE DE PESQUISA")

print(pesquisa_jogo("minecraft"))
print(pesquisa_jogo("gta v"))

# TESTE DE ADIÇÃO

print("\nTESTE DE ADIÇÃO")
print(adicionar_jogo("gta v"))
print(adicionar_jogo("GTA V"))

# TESTE DE REMOÇÃO

print("\nTESTE DE REMOÇÃO")
print(remover_jogo("roblox"))
print(remover_jogo("roblox"))

# TESTE DE POSIÇÃO

print("\nTESTE DE POSIÇÃO")
consultar_posicao(0)
consultar_posicao(10)

# TESTE DE CONTAGEM

print("\nTESTE DE CONTAGEM")
print(contar_jogos(jogos))

# TESTE DE EXIBIÇÃO

print("\nTESTE DE EXIBIÇÃO")
mostrar_jogos()