from time import sleep
from sys import exit
import math

print('\033[35m Operações Matemáticas v0.0.2 \n')

print('''Veja algumas das opções:\n''',
      '-' * 30, '''
[ 1 ] Tabuada de Multiplicação
[ 2 ] Tabuada de Divisão
[ 3 ] Tabuada de Raiz Quadrada
[ 4 ] Sair\n''')

opção = int(input('\033[32mEscolha alguma das opções: - '))

if opção == 1:
    while True:
        print('-' * 30)
        n = int(input('Quer ver a tabuada de qual valor? - '))
        print('\033[33mDigite um número negativo para sair (ex: -1, -2 e etc): -')
        if n < 0:
            print('\033[31mAté a próxima!')
            break
        print(f'\033[33mTabuada de multiplicação para {n}:')
        for c in range(1, 11):
            print(f'{n} × {c} = {n * c}')

elif opção == 2:
    while True:
        print('-' * 30)
        n = int(input('Quer ver a tabuada de divisão de qual valor? - '))
        print('\033[33mDigite um número negativo para sair (ex: -1, -2 e etc): -')
        if n < 0:
            print('\033[31mAté a próxima!')
            break
        print(f'\033[33mTabuada de divisão para {n}:')
        for c in range(1, 11):
            print(f'{n} ÷ {c} = {n / c:.2f}')

elif opção == 3:
    while True:
        print('-' * 30)
        n = int(input('Quer ver a tabuada de raiz quadrada de qual valor? - '))
        print('\033[33mDigite um número negativo para sair (ex: -1, -2 e etc): -')
        if n < 0:
            print('\033[31mAté a próxima!')
            break
        print(f'\033[33mTabuada de raiz quadrada para {n}:')
        for c in range(1, 11):
            print(f'√({n} × {c}) = {math.sqrt(n * c):.2f}')

elif opção == 4:
    print('\033[31mSaindo... Até a próxima!')
    exit()

else:
    print('\033[31mOpção inválida! Reinicie o programa.')
