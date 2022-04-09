# Faça um programa que pergunte o usuário quanto é o seu salário e a % do seu aumento. Calcule o novo salário e printe na tela, além de mostrar quanto aumentou.

salario_antigo = float(input("Qual é o seu salário?"))
aumento_porcentagem = int(input("De quanto foi o aumento em porcentagem?"))
aumento_decimal = aumento_porcentagem / 100
aumento = salario_antigo * aumento_decimal
salario_atual = salario_antigo + aumento
print(f'O seu salário agora é de {salario_atual}. O aumento foi de R${aumento}')
