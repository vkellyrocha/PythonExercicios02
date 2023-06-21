#Ordena um vetor de tamanho 3!
l = [2, 1, 3]
aux = []
if l[0] > l[1] > l[2]:
    aux.append(l)
elif l[0] > l[2] > l[1]:
    aux.append(l[0])
    aux.append(l[2])
    aux.append(l[1])
elif l[1] > l[0] > l[2]:
    aux.append(l[1])
    aux.append(l[0])
    aux.append(l[2])
elif l[1] > l[2] > l[0]:
    aux.append(l[1])
    aux.append(l[2])
    aux.append(l[0])
elif l[2] > l[1] > l[0]:
    aux.append(l[2])
    aux.append(l[1])
    aux.append(l[0])
elif l[2] > l[0] > l[1]:
    aux.append(l[2])
    aux.append(l[0])
    aux.append(l[1])
print(aux)
