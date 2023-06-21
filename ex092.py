'''Escreva uma função que aceita uma string como parâmetro e retorna
um número inteiro. A função deve imprimir o resultado da
subsDtuição de todos os espaços do seu parâmetro pelo caractere ‘-’,
e retorna o número de subsDtuições feitas.'''
valor = input('Digite algo: ')
def conta_substituicao(x):
    cont = 0
    for i in range(len(x)):
        if x[i] == ' ':
            cont += 1
    x = x.replace(' ', '-')
    return cont
print(conta_substituicao(valor))
