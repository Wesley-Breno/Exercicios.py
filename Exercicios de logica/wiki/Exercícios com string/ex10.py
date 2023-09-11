"""
Número por extenso.
Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
"""

# Listas onde serao usados os indices para escrever o numero por extenso
numeros_de_1_a_19 = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
                     'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
                     'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']

dezenas = ['vinte', 'trinta', 'quarenta', 'ciquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

# Enquanto o usuario nao informar um valor numerico entre 1 e 99
while True:
    try:
        numero = int(input('Digite um valor numerico inteiro entre 1 e 99: '))

    except ValueError:
        print('\n\n\t\t[ERRO]: Tente novamente e insira um valor numerico inteiro.\n\n')

    else:
        # Se o numero informado estiver entre 1 e 99
        if 1 <= numero <= 99:
            print('Numero por extenso: ', end='')

            # Se o numero informado pode ser chamado na lista "numeros_de_1_a_19"
            if numero < 20:
                print(numeros_de_1_a_19[numero - 1])
                break

            dezena_valor_informado = str(numero)[0]
            unidade_valor_informado = str(numero)[1]

            # Se o segundo caractere for 0, chama apenas a dezena
            if int(unidade_valor_informado) == 0:
                print(dezenas[int(dezena_valor_informado) - 2])
                break

            # Se o segundo caractere for diferente de 0, pega a dezena correspondente e a unidade
            print(f'{dezenas[int(dezena_valor_informado) - 2]} e {numeros_de_1_a_19[int(unidade_valor_informado) - 1]}')
            break

        else:
            print('\n\n\t\t[ERRO]: Tente novamente e insira um valor entre 1 e 99.\n\n')
