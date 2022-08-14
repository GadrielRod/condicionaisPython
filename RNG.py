import emoji
from random import randint
print('Bem vindo ao sistema de rng\n'
      'Você tem sorte?')
try:
    n = int(input('Digite um número de 1 a 6: '))
    if 0 < n < 7:
        x = randint(1, 6)
        t = 0

        while n != x:
            t += 1
            print(f'Você errou, tentativa: {t}')
            n = int(input('Digite um número de 1 a 6: '))

        else:
            t += 1
            print('Você acertou\n'
                  'Na tentativa {}'.format(t))

    else:
        print('Você digitou um valor númerico fora do intervalo')
except ValueError:
    print('Você digitou um valor invalido')