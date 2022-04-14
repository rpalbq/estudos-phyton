#Escreva um script que leia um número inteiro e informe se ele é ímpar ou par.

valor =  int(input('Digite um número:'))

if valor % 2 == 0:
    print(f'O valor {valor} é par')
else:
    print(f'O valor é ímpar')