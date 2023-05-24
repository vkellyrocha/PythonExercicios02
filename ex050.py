'''Altera o programa anterior para que o usuário digite o número inicial
e final da tabuada para que não inicie necessariamente com 1 e termine em 10.'''
n = int(input('Digite o número no qual você deseja saber a tabuada: '))
i = int(input('Digite o número inicial: '))
f = int(input('Digite o número final: '))
for x in range(i,f+1):
    print(f'{n} x {x} = {n * x}')
