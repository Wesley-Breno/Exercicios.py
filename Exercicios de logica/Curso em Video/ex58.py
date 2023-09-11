"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10.

Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint  # Importando a função que gera numeros aleatorios

tentativas = 0

print(f'\n\n{"Adivinhe o numero que a cpu pensou":^45}')

while True:
    cpu_numero = randint(0, 10)  # Pegando um numero aleatorio de 0 a 10
    print('__' * 20)
    try:
        usuario_numero = int(input('Digite o numero que a cpu pensou: '))
    except:
        print('\n\nERROR\nPor favor digite um valor valido.\n\n')
    else:
        if cpu_numero == usuario_numero:
            print(f'\n\n\033[;1m{"Parabens! Voce acertou ヾ(≧▽≦*)o":^45}\033[m\n{f"Total de tentativas ate acertar: {tentativas}":^45}')
            break
        else:
            tentativas += 1
            print(f'\n\n\033[;1m{"Oh nao! Voce errou ( ´･･)ﾉ(._.`)":^45}\033[m\n{"Nao desanime! tente novamente.":^45}')
