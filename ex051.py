'''Faça um programa que calcule o produto de dois números utlizando a soma.'''
n = int(input('Número: '))
p = int(input('Ele será multiplicado por: '))
aux = n
for x in range(1, p):
    n = n + aux
print(f'O produto vale {n}')
