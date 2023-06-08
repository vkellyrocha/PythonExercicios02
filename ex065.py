# %% Meu chatbot versão 3
print('Olá humano, o que deseja?')

mensagem = ';)'
while(mensagem.find('sair') == -1):
    mensagem = input().lower()
    print('Continue a falar, por favor')
print('Ok, a nossa seção custou 500 reais')
