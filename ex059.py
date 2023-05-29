'''• Escreva um programa que leia um número e verifique se é ou não um
número primo. Para fazer essa verificação, calcule o resto da divisão do
número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões
for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.'''
n = int(input('Digite um número: '))
cont = 0
if n == 0 or n == 1:
    print('Não primo')
elif n == 2:
    print('Primo')
else:
    for x in range(2, n):
        if n % x == 0:
            cont += 1
    if cont == 0:
        print('Primo')
    else:
        print('Não primo')
