"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

valores = []  # Lista que contera todos os valores que o usuario informar
cont = 0  # Contador para informar ao usuario qual valor ele esta digitando

print('\n\n\t\tAdicione a quantidade de numeros que quiser'
      '\n\t\t\tDigite [ 0 ] para parar\n\n')

while True:  # Enquanto o usuario quiser continuar a adicionar valores
    cont += 1

    try:
        numero = int(input(f'Informe o {cont}° valor: '))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe o valor corretamente\n\n')
        cont -= 1

    else:
        if numero == 0:  # Se o usuario decidiu parar de adicionar valores
            break

        valores.append(numero)

if len(valores) > 0:  # Se o usuario adicionou pelo menos 1 valor
    print('\n\n\t\tResultado\n\n'
          f'Valores informados: {valores}\n'
          f'Menor valor: {min(valores)}\n'
          f'Maior valor: {max(valores)}\n'
          f'Soma dos valores: {sum(valores)}')

else:
    print('\n\n\t\tVoce nao informou nenhum numero\n\n')
