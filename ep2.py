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