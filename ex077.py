from random import randint
#Jogo de pedra papel ou tesoura melhorado
print('=+'*20)
print('#Jogo de pedra papel ou tesoura melhorado')
print('Digite: \n1 para pedra\n2 para tesoura\n3 para papel')
print('=+'*20)
n = int(input())
user1 = ''
if n == 1:
    user1 = 'Pedra'
elif n == 2:
    user1 = 'tesoura'
elif n == 3:
    user1 = 'papel'
#recebendo valor do robo
user2 = randint(1,3)
if user2 == 1:
    user2 = 'Pedra'
elif user2 == 2:
    user2 = 'tesoura'
elif user2 == 3:
    user2 = 'papel'
#conferindo valores
if user1 == user2:
    print('Empate')
elif (user1 == 'pedra' and user2 == 'tesoura') or\
    (user1 == 'papel' and user2 == 'pedra')or \
    (user1 == 'tesoura' and user2 == 'papel'):
    print('jogador ganhou')
else:
    print('Robô ganhou')
