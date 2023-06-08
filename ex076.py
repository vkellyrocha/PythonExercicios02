#Desenvolva um algoritmo que faz a média de uma lista
def soma(x):
    soma = 0
    for i in range(len(x)):
        soma = soma + x[i]
    return soma

l = [0, 1, 2, 3, 4, 5]
print(soma(l)/len(l))
