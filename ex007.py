nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1+nota2+nota3) / 3

print('A média do aluno é {:.1f}'.format(media))

if media < 7.0:
    print('O aluno está reprovado!')
else:
    print('O aluno está aprovado!')

