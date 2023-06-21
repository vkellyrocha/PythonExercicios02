'''Faça uma função que retorne o reverso de um número inteiro informado.
Por exemplo: 123 -> 321.'''
def reverso(x):
    aux = []
    for i in range(len(x)):
        aux.append(x[-i-1])
    aux = ''.join(aux)
    return aux
n = input('Digite um número: ')
print(reverso(n))
