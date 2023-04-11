km = float(input('Quer calcular quantos R$ vai gasta em sua viagem, digite os Km : '))
print('Lembrando que valor de 0,50R$ até 200km a cima de 200km e cobrado 0,45R$')
if km <=200:
    print('O valor da sua viagem vai custar {}R$'.format(km * 1/2))
else:
    print('O valor da sua viagem vai custar {}R$'.format(km * 0,45))