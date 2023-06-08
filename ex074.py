#Dado um ano, retorne ao século em que ele está.
#O primeiro século vai do ano 1 até o ano 100 inclusive, o segundo - do ano 101 até o ano 200 inclusive, etc.
ano = int(input('Digite um ano: '))
if ano % 100 == 0:
  print(f'Este é o século: {ano//100}')
else:
  print(f'Este é o século: {(ano//100) + 1}')
