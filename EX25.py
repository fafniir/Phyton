import random
n1 = 1
n2 = 2
n3 = 3
numero = (n1, n2, n3)
sorteio = random.choice(numero)
usuario = int(input('Tente adivinhar em qual numero eu pensei?! de 1 até 3 :'))
if sorteio == usuario:
    print('Parabens!!')
else:
    print('Que pena tente novamente')