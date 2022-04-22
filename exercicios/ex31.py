#Faça um programa que peça uma nota entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input("Digite sua nota:"))

while (nota <= 0) or (nota >= 10 ):
    print("Nota não está entre 0 e 10. Digite a nota corretamente:")
    nota = int(input("Digite a nota:"))

print(f"Sua nota foi {nota}")