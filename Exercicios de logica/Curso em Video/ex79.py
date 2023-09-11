"""
Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente.
"""

valores = []

print('\n\t\t\033[;37mDigite -1 para encerrar\033[m\n\n')
while True:  # Enquanto o usuario nao digitou -1
    print('__' * 15)
    valor = str(input('Digite um valor numerico: '))

    if valor == '-1':  # Se o valor informado for -1, encerra o programa
        break

    if valor.isdigit():  # Se o valor digitado for um numero
        if valor not in valores:  # Se o valor informado nao estiver na lista ainda
            print('valor adicionado\n')
            valores.append(valor)

        else:
            print('valor ja adicionado\n')

    else:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, insira um numero inteiro.\n\n')

if len(valores) > 0:  # Se a lista estiver com valores
    valores.sort()
    print('\n\nValores unicos digitados em ordem crescente;\n'
          f'> {valores}')

else:
    print('\n\n\t\tNenhum valor foi informado :(\n')
