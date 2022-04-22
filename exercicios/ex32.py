#Faça um programa que informe a tabuada

numero = int(input("De qual número você quer a tabuada?"))
cont = 1

while cont <= 10:
    tabuada = numero * cont
    print(f" {numero} X {cont} = {tabuada}")
    cont = cont + 1
    