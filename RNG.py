import emoji
from random import randint
print('Bem vindo ao sistema de rng\n'
      'Você tem sorte?')
try:
    n = int(input('Digite um numero entre 1 e 7, e veja se vai acertar: '))

    if 0 < n < 8:
        for i in range(7):
            x = randint(1, 7)
            print(f'numero usado: {n}; numero gerado aleatoriamente: {x}; tentativa: {i+1}')
            if n == x:
                print(f'Voce acertou um numero, na tentativa {i+1}')

    else:
        print(emoji.emojize('Você digitou um numero diferente do pedido :crying_face:'))
except ValueError:
    print('Você digitou um valor invalido ')