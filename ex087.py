def imprime_lista(l, fimimpressao, fcondicao):
    for e in l:
        if fcondicao(e):
            fimimpressao(e)
def imprime_elemento(e):
    print(f'Valor: {e}')
def epar(x):
    return x % 2 == 0
def eimpar(x):
    return not epar(x)
def primo(z):
    cont = 0
    for x in range(1, z+1):
        if z % x == 0:
            cont += 1
    if cont == 2:
        return 'É primo'
    else:
        return 'Não primo'
l = [1, 7, 9, 2, 11, 0]
imprime_lista(l, imprime_elemento, epar)
imprime_lista(l, imprime_elemento, eimpar)
print(primo(7))

a = lambda x: x * 2
print(a(3))
par = lambda x: x % 2 == 0
print(par(8))
contar_alg = lambda num: len(str(num))
print(contar_alg('ana'))
inverter_num = lambda num: str(num)[::-1]
print(inverter_num(1234))
