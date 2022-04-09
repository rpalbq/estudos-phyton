'''Escreva um programa de ajuda para vendedores. A partir de um valor lido, mostre:
O total a pagar com desconto de 10%
O valor de cada parcela, no parcelamento de 3 x sem juros:
A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
A comissão do vendedor, no caso da venda ser parcelada(5% sobre o valor total)'''

valor = float(input('Digite o valor:'))
valor_com_desconto = valor - (valor * (10/100))
print(f'O valor A VISTA com o desconto de 10% é de R${valor_com_desconto:.2f}') 
parcelamento = valor / 3
print(f'O valor PARCELADO em 3x sem juros SEM o desconto de 10% será de R${parcelamento:.2f} cada parcela')
comissao = int(input('Será parcelado ou a vista? \n1)PARCELADO 2)A VISTA '))

if comissao == 1:
    comissao = valor * (5/100)
elif comissao == 2:
    comissao = valor_com_desconto * (5/100)
else:
    print('Você digitou errado. Inicie o programa novamente.')

print(f'Sua comissão é de R${comissao}')
