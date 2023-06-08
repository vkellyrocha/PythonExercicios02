#Faça um programa que dado uma posição imprima um valor correspondente na sequência de Fibonacci.
posicao = int(input('Digite a posição que deseja: '))
penultimo = 1
ultimo = 1
if posicao > 2:
    posicao -= 2
    for i in range(posicao):
        auxi = ultimo
        ultimo += penultimo
        penultimo = auxi
print(ultimo)
