'''Crie um programa que leia o nome de uma pessoa
e determine se ela tem ou não um nome composto (composto por duas ou mais palavras).'''
nome = input('Digite seu nome: ').split()
if len(nome) > 1:
    print('Composto')
else:
    print('Não é composto')
