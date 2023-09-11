"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

while True:  # Enquanto o usuario nao informar o nome corretamente
    nome = str(input('\nInforme um nome\nNome: '))

    if len(nome) <= 3:  # Se o nome tiver menos de 3 letras
        print('\n\n\t\t\033[;31m[ERRO]\033[m: Informe um nome com mais de 3 letras.\n')

    else:
        break

while True:  # Enquanto o usuario nao informar uma idade entre 0 e 150
    try:
        idade = int(input('\nInforme a idade\nIdade: '))

    except:
        print('\n\n\t\t\033[;31m[ERRO]\033[m: Informe uma idade entre 0 e 150.\n')

    else:
        if 0 <= idade <= 150:  # Se a idade estiver entre 0 e 150
            break

        else:
            print('\n\n\t\t\033[;31m[ERRO]\033[m: Informe uma idade entre 0 e 150.\n')

while True:  # Enquanto o usuario nao informar um salario que seja maior que 0
    try:
        salario = float(input('\nInforme um salario\nSalario: '))

    except:
        print('\n\n\t\t\033[;31m[ERRO]\033[m: Informe um salario que seja maior que 0.\n')

    else:
        if salario > 0:  # Se o salario informado for maior que 0
            break

        else:
            print('\n\n\t\t\033[;31m[ERRO]\033[m: Informe um salario que seja maior que 0.\n')

while True:  # Enquanto o usuario nao informar o sexo
    sexo = str(input('\nInforme o sexo [F - Feminino] . [M - Masculino]\nSexo: ')).upper()

    if sexo == 'F' or sexo == 'M':  # Se o sexo for igual a feminino ou masculino
        break

    else:
        print('\n\n\t\t\033[;31m[ERRO]\033[m: Informe o sexo com a inicial F para feminino ou M para masculino.\n')

while True:  # Enquanto o usuario nao informar um dos estados civis mostrados
    estado_civil = str(input('\nInforme o estado civil\n'
                             'S - Solteiro\n'
                             'C - Casado\n'
                             'V - Viuvo\n'
                             'D - Divorciado\n\nEstado civil: ')).upper()

    if estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D':  # Se informou o estado civil
        break

    else:
        print('\n\n\t\t\033[;31m[ERRO]\033[m: Informe o estado civil com as iniciais mostradas.\n')

print('\n\n\t\tInformações preenchidas com \033[;32msucesso\033[m.\n\n'
      f'Nome: {nome}\n'
      f'Idade: {idade}\n'
      f'Salario: R\033[;32m$\033[m{salario:.2f}\n'
      f'Sexo: {sexo}\n'
      f'Estado civil: {estado_civil}')
