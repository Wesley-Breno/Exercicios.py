"""
Altere o programa anterior para mostrar no final a soma dos números.
"""

while True:  # Enquanto o usuario nao informar os valores corretamente
    try:
        primeiro_valor = int(input('Informe o primeiro valor: '))
        segundo_valor = int(input('Informe o segundo valor: '))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, insira os valores novamente.\n\n')

    else:
        break

soma = 0  # Variavel que ira conter a soma dos numeros

if primeiro_valor < segundo_valor:
    print(f'\n\n\t\tNumeros que estao no intervalo entre {primeiro_valor} e {segundo_valor}\n')

    for c in range(primeiro_valor, segundo_valor + 1):
        if c == primeiro_valor or c == segundo_valor:  # Se o contador estiver no valor informado
            print(f'\033[;31m{c}\033[m', end=' ')

        else:
            print(f'\033[;32m{c}\033[m', end=' ')  # O contador estiver nos numeros que estao no intervalo dos valores

        soma += c

    print(f'\n\n\t\tA soma de todos os numeros equivale a: {soma}\n')

elif primeiro_valor > segundo_valor:
    print(f'\n\n\t\tNumeros que estao no intervalo entre {primeiro_valor} e {segundo_valor}\n')

    for c in range(primeiro_valor, segundo_valor - 1, -1):  # Fazendo contagem decrescente
        if c == primeiro_valor or c == segundo_valor:
            print(f'\033[;31m{c}\033[m', end=' ')

        else:
            print(f'\033[;32m{c}\033[m', end=' ')

        soma += c

    print(f'\n\n\t\tA soma de todos os numeros equivale a: {soma}\n')

else:
    print('\n\n\t\tOs valores informados sao iguais.\n\n')
