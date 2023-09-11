"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
* O produto do dobro do primeiro com metade do segundo.
* A soma do triplo do primeiro com o terceiro.
* O terceiro elevado ao cubo.
"""

numeros_inteiros = []
while True:  # Enquanto o usuario nao digitar os valores corretamente
    for c in range(2):  # Pegando dois numeros inteiros
        try:
            numeros_inteiros.append(int(input(f'Digite o {c + 1}º numero inteiro: ')))
        except:  # Mostrando um erro caso dê errado, e limpando a lista para comecar pegar os numeros de novo
            print('\n\n\t\t\033[;31mDIGITE OS VALORES CORRETAMENTE.\033[m\n')
            numeros_inteiros = []
            break

    if len(numeros_inteiros) == 2:  # Se o usuario informou os dois numeros inteiros
        while True:  # Enquanto o usuario nao informar o numero real
            try:
                numero_real = float(input('Digite um numero real: '))
            except:
                print('\n\n\t\t\033[;31mDIGITE OS VALORES CORRETAMENTE.\033[m\n')
            else:
                break  # Parando a repeticao se o usuario informou o numero real

        break  # Parando o laco principal quando o usuario informou todos os dados pedidos.


# Produto do dobro do primeiro numero com a metade do segundo numero
produto_do_dobro_do_primeiro_com_metade_do_segundo = (numeros_inteiros[0] * 2) * (numeros_inteiros[1] / 2)

# Somando o triplo do primeiro numero com o terceiro numero
soma_do_triplo_do_primeiro_com_o_terceiro = (numeros_inteiros[0] * 3) + numero_real

# Terceiro numero elevado ao cubo
terceiro_elevado_ao_cubo = numero_real ** 3

print('\n\n\t\tResultado\n\n'
      f'|> O produto do dobro do primeiro com metade do segundo: {produto_do_dobro_do_primeiro_com_metade_do_segundo}\n'
      f'|> A soma do triplo do primeiro com o terceiro: {soma_do_triplo_do_primeiro_com_o_terceiro}\n'
      f'|> O terceiro elevado ao cubo: {terceiro_elevado_ao_cubo}\n\n')
