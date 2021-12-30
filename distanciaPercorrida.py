d = float(input('Qual a distância a ser percorrida: Km '))

if d <= 200:
    distNormal = d * 0.50
    print('O valor a ser pago será de R${:.2f} reais'.format(distNormal))
else:
    distLonga = d * 0.45
    print('O valor a ser pago será de R${:.2f} reais'.format(distLonga))
