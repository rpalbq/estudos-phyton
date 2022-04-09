#Faça um programa que peça um número inteiro e verifique se ele é positivo ou negativo
numero = int(input('Digite um número:'))
if numero > 0:
    print(f'O número {numero} é positivo!')
elif numero == 0:
    print(f'O número {numero} é neutro!')
else:
    print(f'O número {numero} é negativo!')