# %% Meu chatbot versão 2
print('Olá humano, o que deseja?')

mensagem = input().lower()

if mensagem.find('olá') > -1:
    print('Eae, beleza?')
elif mensagem.find('dinheiro') > -1:
    print('Dinheiro? Tem não, perdoe')
elif mensagem.find('felicidade') > -1:
    print('Felicidade? Tem não, perdoe')
else:
    print('Oh, imundo')
