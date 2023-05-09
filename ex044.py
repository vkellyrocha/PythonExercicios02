'''Escreva um programa que leia um número inteiro e determine se ele é positivo, negativo ou zero.'''
n1 = int(input('Digite um número inteiro: '))
resp = ''
if n1 > 0:
    resp = 'positivo'
elif n1 < 0:
    resp = 'negativo'
else:
    resp = 'zero'
print(f'O valor digitado é {resp}')
