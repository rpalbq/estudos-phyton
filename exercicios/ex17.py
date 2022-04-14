#Faça um programa que leia 5 notas do enem (linguagens, humanas, natureza, matemáticae redação) e seus respectivos pesos, e imprima a sua média.

linguaguens = float(input('Qual foi a sua nota em linguagens?'))
peso_ling = float(input('Qual é o peso em linguagens?'))
humanas = float(input('Qual foi a sua nota em humanas?'))
peso_hum = float(input('Qual é o peso em humanas?'))
naturezas = float(input('Qual foi a sua nota em naturezas?'))
peso_nat = float(input('Qual é o peso em naturezas?'))
matematica = float(input('Qual foi a sua nota em matemática?'))
peso_mat = float(input('Qual é o peso em matemática?'))
redacao = float(input("Qual foi a sua nota em redação?"))
peso_red = float(input('Qual é o peso em redação?'))

total_pesos = (peso_hum + peso_ling + peso_mat + peso_nat + peso_red)
media_ponderada = ((linguaguens + humanas + naturezas + matematica + redacao) / total_pesos)
print(f'Sua nota foi de  {media_ponderada}')