#Escreva um programa que conta as vogais, espaços e caracteres.
vogais = ['a', 'e', 'i', 'o', 'u', 'ã']
teste = input('Digite algo: ')
cont_v = 0
#contar vogais
for x in range(len(teste)):
    if teste[x] in vogais:
        cont_v = cont_v + 1
quant_caracter = len(teste.replace(' ', ''))
print(f'Quantidade de espaços {len(teste.split()) - 1}')
print(f'A quantidade de vogais é {cont_v}')
print(f'Quantidade de caracteres: {quant_caracter}')
