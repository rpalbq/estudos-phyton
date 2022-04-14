#Faça um programa que peça dois números e informe qual é o maior, qual é o menor e diga também se são iguais ou não.

valor1 = float(input("Digite o valor 1:"))
valor2 = float(input("Digite o valor 2:"))

if valor1 > valor2:
    print(f'O valor {valor1} é MAIOR que o {valor2}')
elif valor2 > valor1:
    print(f'O valor {valor2} é MAIOR que o {valor1}')
else:
    print(f'O valor {valor1} é igual ao valor {valor2}')
