'''Faça um programa que leia e valide a s seguintes informações:
a)  nome: maior que 3 caracteres
b) idade: entre 0 e 150
c) salario: maior que 0'''

nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))
salario = float(input("Digite o seu salário: "))

while (len(nome) <= 3):
    nome = str(input("Seu nome precisa ser maior que 3 caracteres. tente novamente: "))

while (idade <= 0) or (idade >= 150):
    idade = int(input("Sua idade deve ser entre 0 e 150. Digite novamente a sua idade: "))

while salario <= 0:
    salario = float(input("Seu salário precisa ser maior que 0. Digite novamente seu salário: "))


print(f"Seu nome é {nome} sua idade é {idade} e seu salário é R${salario}")

