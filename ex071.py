'''Encontre o menor fatorial que não seja menor que n.
Dado um inteiro n, encontre o mínimo k tal que
k = m! (onde m! = 1 * 2 * ... * m) para algum inteiro m;
k >= n.
'''
n = int(input('Digite um valor: '))
k = 1
cont = 1
while k < n:
    k = k * m
    m = m + 1
print(k)
