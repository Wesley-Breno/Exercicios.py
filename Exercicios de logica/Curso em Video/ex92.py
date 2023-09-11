"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for
diferente de ZERO, o dicionário receberá também o ano de contratação e
o salário. Calcule e acrescente, além da idade, com quantos anos a
pessoa vai se aposentar.
"""
from datetime import date  # Importando modulo para pegar o ano atual

dados = dict()  # Dicionario onde ficara os dados da pessoa
dados['nome'] = str(input('Nome: '))

try:
    dados['ano_nascimento'] = int(input('Ano de nascimento: '))
    dados['c_trabalho'] = int(input('Carteira de trabalho (0 nao tem): '))

except:
    print('\n\n\t\t[ERRO]: Informe os valores corretamente\n\n')

else:

    if dados['c_trabalho'] != 0:  # Se o usuario informou a numeracao da carteira de trabalho
        dados['ano_contratacao'] = int(input('a. contratacao > '))
        dados['salario'] = float(input('salario > '))

        print('---' * 10)
        print(f'''\t\t{dados['nome']}
    
Idade: {int(date.today().year) - dados['ano_nascimento']}
CTPS: {dados['c_trabalho']}
A. contrato: {dados['ano_contratacao']}
Salario: R\033[;32m$\033[m{dados['salario']:.2f}
Aposentadoria:  Faltam {65 - (int(date.today().year - dados['ano_nascimento']))} anos''')

    else:
        print('---' * 10)
        print(f'''\t\t{dados['nome']}
    
Idade: {int(date.today().year) - dados['ano_nascimento']}
CTPS: \033[;37m[NAO TEM]\033[m''')
