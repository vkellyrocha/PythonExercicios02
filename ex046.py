'''Escreva um código em Python que receba uma lista de números inteiros e
retorne True se pelo menos um dos números for par e outro número for ímpar.'''
x = 0
lista = []
cont_par = 0
cont_impar = 0
while x < 5:
    n = int(input('Digite o número: '))
    lista.append(n)
    if n % 2 == 0:
        cont_par = cont_par + 1
    else:
        cont_impar = cont_impar + 1
    x = x + 1
print(cont_par > 0 and cont_impar > 0)
