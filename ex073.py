#Dado um string (texto) cheque se ele é palíndromo.
valor = input('Digite um string: ')
palindromo = True
for x in range(len(valor)):
#confere se são iguais
  if valor[x] == valor[-x-1]:
    palindromo = True
  else:
    palindromo = False
    break
print(f'É palíndromo? {palindromo}')
