from random import randint
n = int(input('Digite um numero entre 0 e 5: '))
x = randint(0, 5)

if n == x:
    print('Você venceu :)')
    print('Seu numero: {}\n'
          'Numero do computador: {}'.format(n, x))
else:
    print('Você perdeu :(')
    print('Seu numero: {}\n'
          'Numero gerado: {}'.format(n, x))
