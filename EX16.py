import random
n1 = input('Primeiro pet? ')
n2 = input('Segundo pet? ')
n3 = input('Terceiro pet? ')
n4 = input('Quarto pet? ')

lista = (n1, n2, n3, n4)
sorteio = random.choice(lista)
print('O pet mais fofinho é {}'.format(sorteio))
