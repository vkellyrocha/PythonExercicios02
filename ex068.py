'''Escreva um código em Python que receba uma lista de números inteiros e retorne True se pelo menos um dos números for par e outro número for ímpar.'''
l = [0, 0, 0, 0]
l[0] = int(input('N°1: '))
l[1] = int(input('N°2: '))
l[2] = int(input('N°3: '))
l[3] = int(input('N°4: '))

cont_par = 0
cont_impar = 0

for x in range(len(l)):
  if l[x] % 2 == 0:
    cont_par += 1
  else:
    cont_impar += 1
print(cont_impar > 0 and cont_par > 0)