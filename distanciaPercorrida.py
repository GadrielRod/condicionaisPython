d = float(input('Qual a distância a ser percorrida: Km '))

if d <= 200:
    distValor = d * 0.50
else:
    distValor = d * 0.45
print('O valor a ser pago será de R${:.2f} reais'.format(distValor))
