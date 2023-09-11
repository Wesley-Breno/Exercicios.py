"""
Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um
valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
OBRIGATÓRIO nas eleições.

Obrigatorio: 18 a 70
Opcional: 16 ou 17 ou maior de 70
Negado: menor de 16
"""

from datetime import date  # Importando a funcao date para pegar o ano atual


def voto(nascimento: int):
    """
    Funcao que recebe o ano de nascimento de uma pessoa e analisa sua idade
    e fala se a pessoa tem obrigacao de votar, opcional ou nao pode votar.
    :param nascimento: Parametro que recebe o ano de nascimento
    :return: None
    """
    ano_atual = date.today().year  # Pegando o ano atual
    idade = ano_atual - nascimento  # Fazendo o calculo para ficar com a idade da pessoa

    print(f'\n\n\t\tCom {idade} anos')
    if 18 <= idade <= 70:  # Tem a idade maior que 18 anos e menor que 70
        print('\tSeu voto é \033[;1mOBRIGATORIO\033[m\n\n')

    elif 16 <= idade <= 17 or idade > 70:  # Tem a idade entre 16 e 17, ou é maior que 70 anos
        print(f'\tSeu voto é \033[;1mOPCIONAL\033[m\n\n')

    else:  # Se for menor que 16 anos
        print('\tSeu voto é \033[;1mRECUSADO\033[m\n\n')


while True:  # Repetindo ate o usuario digitar o ano corretamente
    try:
        ano_nascimento = int(input('Informe o ano de nascimento: '))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe o ano de nascimento novamente.\n\n')

    else:
        voto(ano_nascimento)
        break
