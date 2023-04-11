detran = int(input('Digite a valocidade que você passou? '))
multa = detran - 80
if detran <= 80:
    print('De acordo com a valocidade')
else:
    print('Que pena você vai recebe uma multa no valor de {}'.format(multa * 7), 'R$')
    print('Lembre se sua multa e calculado em 7R$ por cada km ultrapassado ')
