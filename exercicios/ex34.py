numero = int(input("Digite o número que você quer o fatorial: "))
resultado = 1
contador = 1

while contador <= numero:
    resultado = resultado *  contador
    contador = contador + 1
    
print(resultado)