'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que existem descontos que
são: (i) do imposto de Renda, que depende do salário bruto (conforme tabela abaixo), (ii) 3% para o
Sindicato e (iii) INSS de 10%. O FGTS corresponde a 11% do salário bruto, mas não é descontado (é a
empresa que deposita).
O salário líquido corresponde ao salário bruto menos os descontos O programa deverá pedir ao usuário
o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR;
Salário Bruto até R$900,00 (inclusive) – Isento;
Salário Bruto de ate R$ 1500,00 (inclusive) – desconto de 5%;
Salario bruto até R$ 2500,00 (Inclusive) – desconto de 10%;
Salário bruto acima de R$ 2500 – Desconto de 20%.
Imprima na tela as informações, dispostas conforme o exemplo abaixo, no exemplo valor da hora é 5 e
a quantidade de horas é 220.
Saída:
Salário bruto ( R$ 5 * 220h ) : R$ 1100,00
( – ) IR (5%) : R$ 55,00
( – ) INSS (10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de descontos : R$ 165,00
Salário Líquido : R$ 935,00'''

valor_hora = float(input("Qual é o valor da sua hora trabalhada?"))
horas_trabalhadas = float(input("Quantas horas você trabalhou?"))
salario_bruto = (valor_hora * horas_trabalhadas)
desconto_sindicato = ((3/100) * salario_bruto)
desconto_fgts = ((11/100) * salario_bruto)

if (salario_bruto <= 900):
    desconto_renda =  0
    salario_liquido = (salario_bruto - (desconto_sindicato + desconto_renda))

elif (salario_bruto > 900) and (salario_bruto <= 1500):
    desconto_renda =  ((5/100) * salario_bruto)
    salario_liquido = (salario_bruto - (desconto_sindicato + desconto_renda))

elif (salario_bruto > 1500) and (salario_bruto <= 2500):
    desconto_renda =  ((10/100) * salario_bruto)
    salario_liquido = (salario_bruto - (desconto_sindicato + desconto_renda))

elif (salario_bruto > 2500):
    desconto_renda =  ((20/100) * salario_bruto)
    salario_liquido = (salario_bruto - (desconto_sindicato + desconto_renda))
else: 
    print("Não foi possível completar o cálculo, houve algum erro.")

total_desconto = (desconto_renda + desconto_sindicato) 

print(f'O seu salário bruto é de R$ {salario_bruto}')
print(f'O desconto do imposto de renda é de R$ {desconto_renda}')
print(f'O desconto do sindicato é de R${desconto_sindicato:.2f}')
print(f'O desconto do fgts é de R${desconto_fgts} PS: Não é descontado do salário bruto!')
print(f'O total de descontos foi de R${total_desconto}')
print(f'O Salário líquido é de R${salario_liquido}')

