'''Faça um programa de forma a ler um número n. Imprima os n primeiros
números primos.'''
num = int(input('Digite um número: '))
primos = []
x = 2
while len(primos) < num:
    divisores = 0
    for y in range(1, x + 1):
        if x % y == 0:
            divisores += 1
    if divisores == 2:
        primos.append(x)
    x += 1
print(primos)
