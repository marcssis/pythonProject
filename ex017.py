from math import hypot
'''oposto = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hi = (oposto ** 2 + adj ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

oposto = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hi = hypot(oposto, adj)
print('A hipotenusa vai medir {:.2f}'.format(hi))
