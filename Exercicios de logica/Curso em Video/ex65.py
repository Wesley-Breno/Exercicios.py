"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

from time import sleep  # Importando o modulo time com a funcao sleep para fazer o programa 'dormir' por alguns segundos

lista_numeros = []

print('\n\t\tDigite [ 0 ] para mostrar o resultado\n')

while True:  # Enquanto o usuario nao digitar zero
    print('__' * 12)
    try:
        numero = int(input('Digite o numero: '))

    except:
        print('\n\t\t[\033[;31mERRO\033[m] Informe uma valor inteiro novamente.')
        sleep(1.5)

    else:
        if numero == 0:  # Parando a leitura de valores se for digitado zero
            break

        else:
            lista_numeros.append(numero)

if len(lista_numeros) > 0:  # Se o usuario digitou algum valor
    print(f"""\n\n\t\t\033[4;1mResultado\033[m

> Media dos valores: {sum(lista_numeros) / len(lista_numeros):.1f}
> Maior valor: {max(lista_numeros)}
> Menor valor: {min(lista_numeros)}""")

else:
    print(f"""\n\n\t\t\033[4;1mResultado\033[m

> Media dos valores: [\033[;31mNenhum valor digitado\033[m]
> Maior valor: [\033[;31mNenhum valor digitado\033[m]
> Menor valor: [\033[;31mNenhum valor digitado\033[m]""")
