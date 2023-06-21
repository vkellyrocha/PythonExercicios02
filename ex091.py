'''Escreva uma função que, dado o valor da conta de um restaurante,
calcule e exiba a gorjeta do garçom, considerando 10% do valor da
conta.'''
def gorjeta(x):
    gorj = x * 0.1
    return gorj
s = int(input('digite o valor da conta: '))
print(gorjeta(s))