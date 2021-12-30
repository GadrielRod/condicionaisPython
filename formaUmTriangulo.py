v1 = float(input('Digite o 1º segmento: '))
v2 = float(input('Digite o 2º segmento: '))
v3 = float(input('Digite o 3º segento: '))

r3 = v1 + v2
r2 = v1 + v3
r1 = v2 + v3

if r1 > v1 and r2 > v2 and r3 > v3:
    print('Os segmentos {}, {} e {}, resultam em um triangulo'.format(v1, v2, v3))
else:
    print('Os segmentos {}, {} e {}, não resultam em um triangulo'.format(v1, v2, v3))
