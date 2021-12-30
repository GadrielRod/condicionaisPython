v = float(input('Em que velocidade o carro passou: '))
RED = "\033[1;31m"
RESET = "\033[0;0m"
if v <= 80:
    print('O carra está dentro do limite de velocidade permitido')
else:
    valorMulta = v - 80
    print(RED+'Você ultrapassou {:.2f}Km/h do limite máximo permitido, '
          'que era 80Km/h'.format(valorMulta)+RESET)
    print('Você recebeu uma multa no valor de R${:.2f} reais'.format(valorMulta*7))
