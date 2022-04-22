# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações

usuario = str(input("Digite o nome do seu usuário:"))
senha = str(input("Digite a senha:"))

while usuario == senha:
    print("Sua senha precisa ser diferente do usuário")
    senha = str(input("Digite a senha:"))

print("Cadastro aprovado")