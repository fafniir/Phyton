print('Olá, espero que tenha curtido o carro, gostaria de saber quantos Km rodou e quantos dias vc ficou com ele ?')
km = float(input('POderia me informa quantos Km fez com nosso carro? '))
day = int(input('Quantos dias você alugou o carro? '))
pkm = km * 0.15
pday = day * 60
total = pkm + pday
print('O total a paga dos km é R${}, e aluguel dos dias ficou R${} a conta ficou R${}'.format(pkm, pday, (total)))