'''Faça um programa em que o usuário informe o salário recebido e o total gasto com
despesas. Na tela deve ser exibido: “Gastos dentro do orçamento” caso o valor gasto não
ultrapasse o salário do usuário, e “Orçamento estourado” se o valor gasto ultrapassar o
salário do mesmo'''

salario = float(input('Qual o valor do seu salário?'))
gasto = float(input('Quanto você gastou com despesas?'))

if salario > gasto:
    print('Gastos dentro do orçamento')
else:
    print('Orçamento estourado =[ ')