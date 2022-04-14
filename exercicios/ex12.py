'''Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente
ao valor que cada deu para a realização da aposta. Faça a um programa que leia quanto cada
apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor
investido'''

apostador_1 = float(input("Apostador 1, qual valor você deseja apostar?"))
apostador_2 = float(input("Apostador 2, qual valor você deseja apostar?"))
apostador_3 = float(input("Apostador 3, qual valor você deseja apostar?"))
valor_premio = float(input("Qual é o valor total do prêmio?"))

#porcentagem de quanto investiu relacionado ao prêmio total. Regra de três
porcentagem_1 = ((apostador_1 * 100) / valor_premio)
porcentagem_2 = ((apostador_2 * 100) / valor_premio)
porcentagem_3 = ((apostador_3 * 100) / valor_premio)

#número decimal da porcentagem que multiplicado com o valor do prêmio total terá o resultado do prêmio individual relacionado a porcentagem investida
premio_1 = ((porcentagem_1 / 100) * valor_premio)
premio_2 = ((porcentagem_2 / 100) * valor_premio)
premio_3 = ((porcentagem_3 / 100) * valor_premio)

print(f'O apostador 1 investiu R${apostador_1}')
print(f'O apostador 2 investiu R${apostador_2}')
print(f'O apostador 3 investiu R${apostador_3}')
print(f'A porcentagem do investimento em relação ao premio do apostador 1 é de {porcentagem_1}%')
print(f'A porcentagem do investimento em relação ao premio do apostador 2 é de {porcentagem_2}%')
print(f'A porcentagem do investimento em relação ao premio do apostador 3 é de {porcentagem_3}%')
print(f'O valor total do prêmio é de R${valor_premio}')
print(f'O jogador 1 irá ganhar R${premio_1:.3f}')
print(f'O jogador 2 irá ganhar R${premio_2:.3f}')
print(f'O jogador 3 irá ganhar R${premio_3:.3f}')