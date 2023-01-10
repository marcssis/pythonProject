largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite da altura da parede: '))
area = largura * altura
qtd_tinta = area / 2
print('A área da parede é de {}m² quadrados e são necessários {} litros de tinta para pinta-la. '.format(area, qtd_tinta))

