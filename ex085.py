def retangulo(largura, altura, caracter ='*'):
    linha = caracter * largura
    for i in range(altura):
        print(linha)
retangulo(3, 4)
print()
retangulo(largura=3, altura=4)
print()
retangulo(altura=4, largura=3)
print()
retangulo(caracter='-', altura=4, largura=3)
print()
retangulo(3,4, caracter='-')
