'''Crie um programa para exibir a tabuada de multiplicação de um
número digitado pelo usuário. Imprima na tela seguindo o exemplo.'''
n = int(input('Digite o número no qual você deseja saber a tabuada: '))
for x in range(1,11):
    print(f'{n} x {x} = {n * x}')
