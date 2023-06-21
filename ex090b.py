'''Faça uma função que receba uma lista e exiba os elementos da última
metade na frente dos elementos da primeira metade.'''
def reverso(x):
    aux = []
    auxFinal = []
    for i in range(len(x)//2, len(x)):
        aux.append(x[i])
    for e in range(0, len(x)//2):
        auxFinal.append(x[e])
    resultado = aux + auxFinal
    return resultado
l = [1, 7, 9, 2, 11, 0]
print(reverso(l))
