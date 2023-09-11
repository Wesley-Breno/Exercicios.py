"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e
seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
magro, além da média das alturas e dos pesos dos clientes
"""
clientes = []

print('\n\n\t\t\033[;37mDigite [ 0 ] para parar de adicionar clientes.\033[m\n')


while True:  # Enquanto o usuario nao informar todos os dados corretamente.
    while True:  # Enquanto o usuario nao informar o id
        try:
            print()
            print('__' * 20)
            codigo_id = int(input('Informe o seu codigo de identificação\nCodigo: '))
        except:
            print('\n\n[\033[;31mERRO\033[m]: Informe o seu codigo de identificação corretamente.\n\n')
        else:
            break

    if codigo_id == 0:  # Se o usuario decidiu encerrar
        break

    while True:  # Enquanto o usuario nao informar a altura
        try:
            altura = float(input('\nInforme a sua altura\nAltura: '))
        except:
            print('\n\n[\033[;31mERRO\033[m]: Informe a sua altura corretamente.\n\n')
        else:
            break

    while True:  # Enquanto o usuario nao informar o peso
        try:
            peso = float(input('\nInforme o seu peso\nPeso: '))
        except:
            print('\n\n[\033[;31mERRO\033[m]: Informe o seu peso corretamente.\n\n')
        else:
            break

    clientes.append([codigo_id, altura, peso])

alturas = []
pesos = []
for c in range(len(clientes)):  # Pegando os pesos e alturas
    pesos.append(clientes[c][2])
    alturas.append(clientes[c][1])

cliente_mais_alto = None
cliente_mais_baixo = None
cliente_mais_gordo = None
cliente_mais_magro = None

for c in range(len(clientes)):  # Colocando os clientes especificos dentro de variaveis
    if clientes[c][1] == max(alturas):
        cliente_mais_alto = clientes[c][:].copy()

    if clientes[c][1] == min(alturas):
        cliente_mais_baixo = clientes[c][:].copy()

    if clientes[c][2] == max(pesos):
        cliente_mais_gordo = clientes[c][:].copy()

    if clientes[c][2] == min(pesos):
        cliente_mais_magro = clientes[c][:].copy()

print('\n\t\t[ Cliente mais alto ]')
print(f'[ID] = {cliente_mais_alto[0]}\n'
      f'[Altura] = {cliente_mais_alto[1]}\n'
      f'[Peso] = {cliente_mais_alto[2]}')

print('\n\t\t[ Cliente mais baixo ]')
print(f'[ID] = {cliente_mais_baixo[0]}\n'
      f'[Altura] = {cliente_mais_baixo[1]}\n'
      f'[Peso] = {cliente_mais_baixo[2]}')

print('\n\t\t[ Cliente mais gordo ]')
print(f'[ID] = {cliente_mais_gordo[0]}\n'
      f'[Altura] = {cliente_mais_gordo[1]}\n'
      f'[Peso] = {cliente_mais_gordo[2]}')

print('\n\t\t[ Cliente mais magro ]')
print(f'[ID] = {cliente_mais_magro[0]}\n'
      f'[Altura] = {cliente_mais_magro[1]}\n'
      f'[Peso] = {cliente_mais_magro[2]}')

print(f'\n\nMedia das alturas: {sum(alturas) / len(alturas):.2f}\n'
      f'Media dos pesos: {sum(pesos) / len(pesos):.2f}')
