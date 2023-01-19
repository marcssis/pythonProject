import random
a1 = input('Primeiro nome: ')
a2 = input('Digite o segundo nome: ')
a3 = input('Digite o terceiro nome: ')
lista = [a1, a2, a3]
escolhido = random.choice(lista)
print('O escolhido foi: {}'.format(escolhido))



