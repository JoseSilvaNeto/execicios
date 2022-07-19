lar = float(input(' qual a largura da sua parade? '))
alt = float(input(' qual a altura da sua parade?:'))
mq = lar * alt
print('sua parade tem de largura {} e de altura {} sua parde tem {:.2f} m2'.format(lar, alt, mq))
print('voce vai unas {:.2f} litros de tinta para pintar'.format(mq / 2))