#Faça um programa que informe os valores do inicio, de salto e o fim e faça a contagem

inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
salto = int(input("De quanto em quanto o número irá saltar?"))

if inicio <= fim:
    while inicio <= fim:
        print(inicio)
        inicio = inicio + salto
else:
    while inicio >= fim:
        print(inicio)
        inicio = inicio - salto 

