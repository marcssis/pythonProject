qtd_km = float(input('Digite a quilometragem rodada: '))
qtd_dias = int(input('Digite a quantidade de dias que o veículo foi utilizado: '))
km = qtd_km * 0.15
dia = qtd_dias * 60
total = km + dia
print('')
print('O total de dias rodados foi {} e a quilometragem rodada foi: {}.'. format(qtd_dias, qtd_km))
print('No total de dias você pagará R${:.2f} e pagará R${:.2f} pelo total de km rodados!'.format(dia, km))
print('')
print('O valor total ficou: R${}. Muito obrigado por nos escolher e até a próxima!'.format(total))
