v1 = float(input('Digite o comprimento da 1º reta: '))
v2 = float(input('Digite o comprimento da 2º reta: '))
v3 = float(input('Digite o comprimento da 3º reta: '))

r1 = v1 + v2
r2 = v1 + v3
r3 = v3 + v2

if r1 > v3 and r2 > v2 and r3 > v1:
    print('Os comprimentos {}, {} e {}, resultam em um triangulo'.format(v1, v2, v3))
else:
    print('Os comprimentos {}, {} e {}, não resultam em um triangulo'.format(v1, v2, v3))



