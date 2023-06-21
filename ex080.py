'''As pistas de um tesouro são dadas por uma matriz,
com endereço atual e o próximo, liste os passos para alcançar o tesouro.
Exemplo:
Entrada: [[0, 3], [1, 2], [2, X], [3, 1]].
Saída: 0, 3, 1, 2, X
'''
#definindo a matriz
pistas = [[0, 3], [1, 2], [2, 'X'], [3, 1]]
trilha = []
i = 0
while len(pistas)>i:
#se i == 0 então pistas[0][0] == 0
#vai analizar se a linha 0 e coluna 0
#e conferir se é == 0
#caso for verdade, encontramos o ponto de partida
    if pistas[i][0] == 0:
        trilha.append(pistas[i][1])#trilha[] recebe pistas[i][1], ficando trilha[3]
        break
    i += 1
'''O segundo lool é usado para percorrer a trilha até encontrar o tesouro, representado pelo valor X.
condição do loop é verificar se o último elemento da lista 'trilha' é diferente de ' X'
Indicando que o tesouro ainda não foi encontrado
'''
while trilha[-1] != 'X':
    if not(pistas[trilha[-1]][1] in trilha):
        trilha.append(pistas[trilha[-1]][1])
