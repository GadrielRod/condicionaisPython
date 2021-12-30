n1 = float(input('Digite o 1º numero: '))
n2 = float(input('Digite o 2º numero: '))
n3 = float(input('Digite o 3º numero: '))

if n1 >= n3 >= n2:
    print('Entre "{}", "{}" e "{}"'.format(n1, n2, n3))
    print(f'O maior valor é: {n1}')
    print(f'O menor valor é: {n2}')
elif n1 >= n2 >= n3:
    print('Entre "{}", "{}" e "{}"'.format(n1, n2, n3))
    print(f'O maior valor é: {n1}')
    print(f'O menor valor é: {n3}')
elif n2 >= n3 >= n1:
    print('Entre "{}", "{}" e "{}"'.format(n1, n2, n3))
    print(f'O maior valor é: {n2}')
    print(f'O menor valor é: {n1}')
elif n2 >= n1 >= n3:
    print('Entre "{}", "{}" e "{}"'.format(n1, n2, n3))
    print(f'O maior valor é: {n2}')
    print(f'O menor valor é: {n3}')
elif n3 >= n2 >= n1:
    print('Entre "{}", "{}" e "{}"'.format(n1, n2, n3))
    print(f'O maior valor é: {n3}')
    print(f'O menor valor é: {n1}')
elif n3 >= n1 >= n2:
    print('Entre "{}", "{}" e "{}"'.format(n1, n2, n3))
    print(f'O maior valor é: {n3}')
    print(f'O menor valor é: {n2}')


'''menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')'''
