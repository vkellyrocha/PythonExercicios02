'''• Escreva um programa que exiba uma lista de opções (menu): adição,
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
 Repita até que a opção saída seja escolhida.'''
i = 0
while i == 0:
    print('Menu')
    print('-----------------------')
    print('Adição (+) digite 1')
    print('Subtração (-) digite 2')
    print('Multiplicação (×) digite 3')
    print('Divisão (÷) digite 4')
    print('Digite 5 para sair')
    resp = int(input())
    for x in range(1,11):
        if i == 1:
            break
        print('-+'*20)
        for y in range(1,11):
            if resp == 1:
                print(f'{x} + {y} = {x+y}')
            elif resp == 2:
                print(f'{x} - {y} = {x-y}')
            elif resp == 3:
                print(f'{x} x {y:} = {x*y}')
            elif resp == 4:
                print(f'{x} ÷ {y} = {x/y}')
            elif resp == 5:
                i = 1
                break
