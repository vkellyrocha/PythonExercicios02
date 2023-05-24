'''Faça um programa que recebe N números digitados pelo usuário, em
que N também é informado pelo usuário e informe a soma e a média
deles, além do maior e do menor número digitados.'''
x = 1
soma = 0
quant = int(input('Quantos números quer digitar? '))
while x <= quant:
    n = int(input(f'Digite a {x}° nota: '))
    soma = soma + n
    x = x + 1
print(f'Soma: {soma:5.2f}')
print(f'Média: {soma/quant:5.2f}')