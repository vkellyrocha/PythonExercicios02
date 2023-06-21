'''Retorne o valor:
a. máximo
b. mínimo
'''

def minimo(lista):
    mmin = lista[0]
    for x in range(len(lista)):
        if mmin > lista[x]:
            mmin = lista[x]
    return mmin
def maximo(lista):
    mmax = lista[0]
    for x in range(len(lista)):
        if mmax < lista[x]:
            mmax = lista[x]
    return mmax

l = [0, 7, 0, 1, 3, 2, 3, 4, 5]
print(minimo(l))
print(maximo(l))