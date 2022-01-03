frase = str(input('Digite uma frase qualquer: '))

# voltar ao normal
reset = "\033[0m"

bold = "\033[1m"
underline = "\033[4m"
negative = "\033[7m"

c_black = "\033[30m"
c_red = "\033[31m"
c_green = "\033[32m"
c_yellow = "\033[33m"
c_blue_dark = "\033[34m"
c_purple = "\033[35m"
c_blue = "\033[36m"
c_grey = "\033[37m"
c_white = "\033[97m"

bg_black = "\033[40m"
bg_red = "\033[41m"
bg_green = "\033[42m"
bg_yellow = "\033[43m"
bg_blue_dark = "\033[44m"
bg_purple = "\033[45m"
bg_blue = "\033[46m"
bg_grey = "\033[47m"
bg_white = "\033[107m"


print('Style')
print(bold+frase+reset)
print(underline+frase+reset)
print(negative+frase+reset)

print('\nText')
print(c_black+frase+reset)
print(c_red+frase+reset)
print(c_green+frase+reset)
print(c_yellow+frase+reset)
print(c_blue_dark+frase+reset)
print(c_purple+frase+reset)
print(c_blue+frase+reset)
print(c_grey+frase+reset)
print(c_white+frase+reset)

print('\nBack')
print(bg_black+frase+reset)
print(bg_red+frase+reset)
print(bg_green+frase+reset)
print(bg_yellow+frase+reset)
print(bg_blue_dark+frase+reset)
print(bg_purple+frase+reset)
print(bg_blue+frase+reset)
print(bg_grey+frase+reset)
print(bg_white+frase+reset)

teste1 = "\033[1;41m"
teste2 = "\033[4;33;44m"
teste3 = "\033[1;35;43m"
teste4 = "\033[1;42m"
teste5 = "\033[m"
teste6 = "\033[7;40m"

print('\n')
print(teste1+frase+reset)
print(teste2+frase+reset)
print(teste3+frase+reset)
print(teste4+frase+reset)
print(teste5+frase+reset)
print(teste6+frase+reset)

nome = 'Gabriel'

cores = {'azul': '\033[1;34m',
         'vermelho_inv': '\033[7;41m',
         'limpar': '\033[m'}

print('\033[1;31;42mOlá mundo!\033[m, \033[1;30;45mEstou mudando de cor\033[m')
print('Olá {}{}{} prazer em te conhecer'.format('\033[1;31m', nome, '\033[m'))
print('Olá {}mais{} uma vez {}{}{}'.format(c_blue, reset, c_yellow, nome, reset))
print('Olá pela {}ultima{} vez {}{}{}'.format(cores['vermelho_inv'], cores['limpar'], cores['azul'], nome, reset))
