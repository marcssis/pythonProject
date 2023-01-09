from math import sqrt

'''import math
n = float(input('Digite um número e veja seu dobro, triplo e sua raiz quadrada: '))
dobro = n*2
triplo = n*3
raiz = math.sqrt(n)

print('Você escolheu o número {}, seu dobro é {}, seu triplo é {} e sua raiz é {}.'.format(n, dobro, triplo, raiz))'''

n = int(input('Digite um número e veja seu dobro, triplo  raiz quadrada: '))
print('Você digitou o número {}, seu dobro é {}, seu triplo é {} e a raiz é {:.2f}'.format(n, (n*2), (n*3), sqrt(n)))

'''RAIZ QUADRADA
n ** (1/2)
'''