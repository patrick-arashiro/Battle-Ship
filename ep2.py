def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_ocupacao = []
    if orientacao == 'vertical':
        for i in range(0,tamanho):
            lista_ocupacao.append([linha+1, coluna])

    if orientacao == 'horizontal':
        for j in range(0, tamanho):
            lista_ocupacao.append([linha,coluna +j])
    return lista_ocupacao