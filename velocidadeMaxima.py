v = float(input('Em que velocidade o carro passou: '))

if v <= 80:
    print('O carra está dentro do limite de velocidade permitido')
else:
    valorMulta = v - 80
    print('Você ultrapassou {}Km/h do limite maximo permito, que era 80Km/h'.format(valorMulta))
    print('Você recebeu uma multa no valor de R${:.2f} reais'.format(valorMulta*7))