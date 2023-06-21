lista = ['A', 'E', 'I', 'O', 'U']
print(lista[0])
print(lista[2])
print(lista[-1])
#intervalos de listas
print(lista[-5:-2])
print(lista[:2])
print(lista[2:])
print(lista)#saída
lista.append('B')#Adicionar a lista
print(lista)
lista.pop() #Remover elemento do último índice
print(lista)
lista.pop(2)#Remover elemento do índice 2
print(lista)
lista.insert(2, 'I')#Adicionar elemento I no índice 2
print(lista)
del lista[1]#Remover elemento do índice 1
print(lista)
lista.remove('A')#Remover elemento A
print(lista)
#Para verificar se um elemento existe em uma lista use o in
#Se existir você pode capturar onde com index.