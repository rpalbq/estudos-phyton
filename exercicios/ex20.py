'''Faça um algoritmo que ao receber o salário atual de um funcionário, calcule o reajuste do
novo salário de acordo com a seguinte tabela:

Salário atual                    - Reajuste (Aumento)
Abaixo de R$ 1212,00             - 20%
De R$ 1212,00 até R$2000,00      - 15%
Acima de R$ 2000,00              - 10%'''

salario_atual = float(input('Digite o salário atual:'))

if salario_atual < 1212.00:
    reajuste = ((20/100) * salario_atual)
elif (salario_atual >= 1212.00) and (salario_atual <= 2000.00):
    reajuste = ((15/100) * salario_atual)
else:
    reajuste = ((10/100) * salario_atual)

novo_salario = (salario_atual + reajuste)

print(f'Com o aumento de R${reajuste} seu novo salário é de R${novo_salario}')