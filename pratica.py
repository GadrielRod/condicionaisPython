tempo = int(input('Quantos anos tem seu carro: '))
if tempo <= 4:
    print('Carro novo')
else:
    print('Carro velho')

print('--FIM--')

# forma if em uma linha

print('carro novo' if tempo <= 3 else'carro velho')

nome = str(input('Qual seu nome: ')).lower().strip()
if nome == 'Gabriel'.lower():
    print('Seu nome é gabriel')
else:
    print('Seu nome não é gabriel')
