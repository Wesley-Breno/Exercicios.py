"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente. Ao final,
mostre o conteúdo das três listas geradas.
"""

valores_pares = []
valores_impares = []
valores = []

print('\n\n\t\t\033[;37mDigite -1 pra parar de adicionar valores\033[m\n')

while True:  # Enquanto o usuario nao digitar -1
    print('__' * 10)
    valor = str(input('Digite o valor: '))

    if valor == '-1':  # Se o usuario decidiu parar de adicionar valores
        break

    if valor.isdigit():  # Se o valor digitado for um numero
        valores.append(int(valor))

        if int(valor) % 2 == 0:  # Se for par
            valores_pares.append(int(valor))

        else:  # Se for impar
            valores_impares.append(int(valor))

    else:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, insira um numero inteiro novamente.\n\n')

print('\n\n\t\t\033[;1mResultado\033[m\n'
      f'\n> Valores digitados: {valores if len(valores) > 0 else "Nenhum valor digitado"}'
      f'\n> Valores pares digitados: {valores_pares if len(valores_pares) > 0 else "Nenhum valor par digitado"}'
      f'\n> Valores impares digitados: {valores_impares if len(valores_impares) > 0 else "Nenhum valor impar digitado"}'
      f'\n\n')
