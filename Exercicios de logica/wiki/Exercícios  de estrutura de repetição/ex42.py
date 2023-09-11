"""
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
"""

numeros = []  # Lista onde ficara todos os numeros
intervalos = dict()  # Dicionario onde ira conter cada numero em seu intervalo
intervalos['0-25'] = []
intervalos['26-50'] = []
intervalos['51-75'] = []
intervalos['76-100'] = []

print('\n\n\t\t\033[;37mDigite um numero negativo para encerrar a entrada de dados\033[m\n\n')

while True:  # Enquanto o usuario noa digitar um numero que seja negativo
    try:
        numero = int(input('Digite um numero: '))

        if numero < 0:
            break
        else:
            numeros.append(numero)

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe um numero valido.\n\n')

# Adicionando cada numero em seu intervalo
for num in numeros:
    if num >= 0 and num <= 25:  # Se o numero estiver no intervalo entre 0 e 25
        if num not in intervalos['0-25']:  # Se o numero digitado nao estiver na lista ainda
            intervalos['0-25'].append(num)

    elif num >= 26 and num <= 50:
        if num not in intervalos['26-50']:
            intervalos['26-50'].append(num)

    elif num >= 51 and num <= 75:
        if num not in intervalos['51-75']:
            intervalos['51-75'].append(num)

    elif num >= 76 and num <= 100:
        if num not in intervalos['76-100']:
            intervalos['76-100'].append(num)

print(f"""
        Resultado

Numeros no intervalo de 0-25: {intervalos['0-25']}
Numeros no intervalo de 26-50: {intervalos['26-50']}
Numeros no intervalo de 51-75: {intervalos['51-75']}
Numeros no intervalo de 76-100: {intervalos['76-100']}""")
