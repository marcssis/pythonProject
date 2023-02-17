num = int(input('Digite um numero de 1000 a 9999: '))

print('Analisando o numero...')
n = str(num)

print('A unidade é: {}'.format(n[3]))
print('A dezena é: {}'.format(n[2]))
print('A centena é: {}'.format(n[1]))
print('O milhar é: {}'.format(n[0]))
