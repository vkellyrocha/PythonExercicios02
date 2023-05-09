'''Escreva um código em Python que receba uma string e retorne True
se a string contiver pelo menos uma letra maiúscula e pelo menos uma letra minúscula.'''
teste = input('Digite uma string: ')
cont_maius = 0
cont_minus = 0
for x in teste:
    if x == x.upper():
        cont_maius = cont_maius + 1
    else:
        cont_minus = cont_minus + 1
print(cont_minus > 0 and cont_maius > 0)

