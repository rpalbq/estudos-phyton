#Faça um programa que peça o ano que o usuário nasceu e com essa variável calcule a idade da pessoa. Se tiver maior que 18 diga que é maior de idade.

ano_nascimento = int(input('Em que ano você nasceu?'))

if ano_nascimento <= 2022:
    idade =  2022 - ano_nascimento
    print(f'Sua idade é de {idade} anos')
    if idade >= 18:
        print('Você é maior de idade!')
    else:
        print('Você é menor de idade!')
else:
    print('Você nem nasceu ainda!')