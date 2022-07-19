vlr = float(input('o valor do produto e?:'))
des = int(input('o descon e de:'))
nvlr = vlr - (vlr *des /100)


print('o valor do produto e {:.2f}R$ e o valor do desconto e {}% e o novo valor e {:.2f}R$'.format(vlr,des,nvlr))