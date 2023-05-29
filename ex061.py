'''Escreva um programa que verifique se um número é palíndromo.
Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
Exemplos: 454, 10501'''
n = (input('Digite valor: '))
lista = []
cont = 0
for x in range(len(n)):
#se for diferente
    if not(n[x] == n[-x-1]):
        cont = cont + 1
if cont > 0:
    print('Não é palíndromo')
else:
    print('É palíndromo')
    