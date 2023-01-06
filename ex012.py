preco = float(input('Digite o valor do produto e veja o desconto: R$'))
nv_preco = preco - (preco*5/100)
print('O valor inicial é R${} e com desconto fica R${}!'.format(preco, nv_preco))
