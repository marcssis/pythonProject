real = float(input('Digite quanto você tem na carteira: R$ '))
dolar = real/5.26

print('Você tem R${:.2f} na carteira, sendo assim, pode comprar US${:.2f} em dolar.'.format(real, dolar))

