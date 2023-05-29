# %% Meu chatbot versão 1
print('Olá humano, o que deseja?')

mensagem = input().lower()

if mensagem.find('olá') > -1:
    print('Eae, beleza?')
else:
    print('Oh, imundo')

if mensagem.find('dinheiro') > -1:
    print('Dinheiro? Tem não, perdoe')
if mensagem.find('felicidade') > -1:
    print('Felicidade? Tem não, perdoe')
