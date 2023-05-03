def define_posicoes(linha,coluna,orientacao,tamanho):
    lista = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            posicao = []
            posicao.append(linha+i)
            posicao.append(coluna)
            lista.append(posicao)

    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicao = []
            posicao.append(linha)
            posicao.append(coluna+i)
            lista.append(posicao)
    return lista

def preenche_frota(frota, navio, linha, coluna,orientacao, tamanho):
    lista = []
    if orientacao == 'vertical':
        for i in range(0, tamanho):
            lista.append([linha + i, coluna])

    if orientacao == 'horizontal':
        for i in range(0, tamanho):
            lista.append([linha, coluna + i])

    if navio in frota and lista != []:
        frota[navio] += [lista]

    if navio not in frota and lista != []:
        frota[navio] = [lista]

    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro


def posiciona_frota(infos_navios):
    tabuleiro = []
    for i in range(0,10):
        lista = []
    
        for i in range(0,10):
            lista.append(0)
        tabuleiro.append(lista)

    for posicoes in infos_navios.values():
        for posicao in posicoes:
            for posicao_exata in posicao:
                tabuleiro[posicao_exata[0]][posicao_exata[1]] = 1
    return tabuleiro