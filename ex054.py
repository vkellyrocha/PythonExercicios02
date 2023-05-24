'''informe quantos números quer digitar e depois calcule a média de todos os números digitados.'''
x = 1
soma = 0
quant = int(input('Quantos números quer digitar? '))
while x <= quant:
    n = int(input(f'Digite a {x}° nota: '))
    soma = soma + n
    x = x + 1
print(f'Média: {soma/quant:5.2f}')