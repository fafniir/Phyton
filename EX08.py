print('Bem vindo ao Transformado de metros')
print('Digite 1 para transforma em Km ')
print('Digite 2 para transforma em cm')
sim = int(input())

if sim == (1):
    print('digite quantos metro deseja transforma em Km')
    km = float(input('Digite a distancia para Km '))
    print('A distancia de {}m, para Km é {}'.format((km), (km/1000)))

else:
    print('digite quantos metro deseja transforma em cm')
    cm = float(input('Digite a distancia para cm '))
    print('A distancia de {}m, para Cm é {}'.format((cm), (cm*100)))


