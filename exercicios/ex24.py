'''Escreva	 um	 programa	 para	 ler	 o	 ano	 de	 nascimento	 de	 uma	 pessoa	 e	
escrever	 uma	 mensagem	 que	 diga	 se	 ela	 poderá	 ou	 não	 votar	 este	 ano	
(não	é	necessário	considerar	o	mês	em	que	ela	nasceu). '''

anoNascimento = int(input('Em que ano você nasceu?'))
idade = (2022 - anoNascimento)
print(idade)

if idade >= 18:
    print('É obrigatório votar!')
else:
    if idade >= 16 and idade < 18:
        print('Você pode votar, porém não é obrigatório!')
    else:
        print('Você não está apto a votar!')