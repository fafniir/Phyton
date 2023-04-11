n = int(input('Digite um numero e vou dizer se é par ou ímpar :'))
resultado = n % 2
if resultado == 1:
    print('O {} que você digitou é ímpar'.format(n))
else:
    print('O {} que você digitou é par'.format(n))