sal = float(input('qual o valor do seu dalario? R$'))
al = int(input('qual o valor do seu almemto'))
nsal = sal + (sal * al / 100)
print('seu salario era de {:.2f}R$ e com o almento de{} % o novo salario e de {:.2f}R$'.format(sal,al,nsal))
