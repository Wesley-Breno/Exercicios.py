"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

while True:
    cedulas = [50, 20, 10, 1]  # Notas que o banco pode dar
    total = 0  # Variavel que sera usada para comparar com o valor pedido
    cont = 0  # Variavel responsavel para trocar de notas
    notas = {0: 0, 1: 0, 2: 0, 3: 0}  # Chave equivale ao indice da cedula do banco. Valores, quantas vezes foram usadas

    print('\n' * 2)
    print('__' * 14)

    try:
        valor = int(input('Digite o valor a ser sacado\nValor: R\033[;32m$\033[m '))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe o numero inteiro novamente.\n\n')

    else:
        while True:  # Enquanto o programa nao calcular quantas notas serao usadas.
            total += cedulas[cont]  # Somando com a nota da vez.

            if total > valor:  # Se a soma da nota da vez for maior que o valor pedido.
                total -= cedulas[cont]  # Tira a soma da nota da vez
                cont += 1  # Troca de nota
            else:
                notas[cont] += 1  # Contando quantas notas foram usadas na nota da vez

            if total == valor:  # Se for o valor certo
                break
            else:
                total += cedulas[cont]  # Somando o total com a nota da vez

                if total > valor:  # Se for maior, subtraia a nota da vez
                    total -= cedulas[cont]
                else:
                    notas[cont] += 1  # Contando quantas notas foram usadas

        print('--' * 10)
        print(f"""  Valor sacado
    R\033[;32m$\033[m{valor}
        """)
        if notas[0] > 0:  # Se o programa usou nota de 50
            print(f'{notas[0]} Nota de R\033[;32m$\033[m 50')
        if notas[1] > 0:  # Se o programa usou nota de 20
            print(f'{notas[1]} Nota de R\033[;32m$\033[m 20')
        if notas[2] > 0:  # Se o programa usou nota de 10
            print(f'{notas[2]} Nota de R\033[;32m$\033[m 10')
        if notas[3] > 0:  # Se o programa usou nota de 1
            print(f'{notas[3]} Nota de R\033[;32m$\033[m 1')
        print('--' * 10)

        break
