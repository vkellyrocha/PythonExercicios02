'''Faça uma função que receba uma lista e exiba os elementos da última
metade na frente dos elementos da primeira metade.'''
def troca(lista):
    metade = len(lista)//2
    pt1 = []
    pt2 = []
    nova_lista = []
    for x in range(metade):
        pt1 = lista[x]
    for y in range(metade,len(lista)):
        pt2 = lista[y]
    nova_lista = pt1 + pt2
    return nova_lista
l = [1, 7, 9, 2, 11, 0]
print(troca(l))
