salario = float(input('Qual o salário do funcionario: R$'))

if salario > 1250:
    aumSup = salario + (salario * (10 / 100))
    print('Seu novo salário é de: R$ {:.2f} reais'.format(aumSup))
else:
    aumInf = salario + (salario * (15 / 100))
    print('Seu novo salário é de: R$ {:.2f} reais'.format(aumInf))
