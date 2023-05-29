'''Verifique se uma string está contida em outra'''
var1 = input('Digite uma string: ').lower()
var2 = input('Digite outra string: ').lower()
if var1.find(var2) >= 0:
    print(f'A segunda variável está contida na primeira')
else:
    print(f'A variável não está condida em outra')