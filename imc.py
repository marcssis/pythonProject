peso = float(input('Digite o seu peso: '))
alt = float(input('Digite a sua altura: '))
imc = peso / (alt * alt)
print('O seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Seu icm está abaixo do normal')
elif imc <= 24.9:
    print('Seu peso está normal!')
elif imc <= 29.9:
    print('Você está com excesso de peso! Cuidado!')
elif imc <= 34.9:
    print('Obesidade classe 1!')
elif imc <= 39.9:
    print('Obesidade classe 2!')
elif imc >= 40:
    print('Obesidade classe 3!')


