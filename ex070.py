'''Escreva um código em Python que receba um número inteiro e retorne True se o número for primo, ou False caso contrário.'''
num = int(input('Digite um número: '))
divisor = 0
for x in range(1, num+1):
  if num % x == 0:
    divisor = divisor + 1
print(divisor == 2)