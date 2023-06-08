'''Escreva um código em Python que receba uma string e retorne True se a string contiver pelo menos uma letra maiúscula e pelo menos uma letra minúscula.'''
n = input('Digite algo: ')
minus = 0
maius = 0
for x in n:
  if x == x.lower():
    minus = minus + 1
  elif x == x.upper():
    maius = maius + 1
print(minus > 0 and maius > 0)