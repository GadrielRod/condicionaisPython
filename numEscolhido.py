from random import randint
from time import sleep
x = randint(0, 5)
n = int(input('Adivinhe o número que eu pensei entre 0 e 5: '))
print('Você...')
sleep(2)
if n == x:
    print('Você venceu :)')
    print('Seu numero: {}\n'
          'Numero que eu pensei: {}'.format(n, x))
else:
    print('Você perdeu :(')
    print('Seu numero: {}\n'
          'Numero que eu pensei: {}'.format(n, x))
