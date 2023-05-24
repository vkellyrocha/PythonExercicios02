'''Faça um programa para calcular a divisão indicando o quociente e o
resto. Utilize apenas a adição e subtração para chegar ao resultado.'''
n = float(input('Digite um número: '))
d = int(input('Ele será dividido por: '))
cont = 0
auxi = n
while n >= d:
    n = n - d
    cont = cont + 1
print(f'A divisão de {auxi} por {d} resulta no quociente {cont} com resto {n}')
