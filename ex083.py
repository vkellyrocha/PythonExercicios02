a = 5
def muda_e_imprime():
    global a
    a = 7
    print(f'A dentro da função {a}')
print(f'Antes de mudar: {a}')
muda_e_imprime()
print(f'A depois de mudar: {a}')
