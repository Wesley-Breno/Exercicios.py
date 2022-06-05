"""
Exercício para fazer um algoritmo que o usuário coloque um CPF,
e diga se o mesmo é valido ou não.
"""

from functions import programa_encerrado, erro, linha  # Funções que criei.

print(f'\n\n\033[;37m{"Digite [ 0 ] para encerrar.":^45}\033[m\n\n')

while True:  # Enquanto o usuario nao digitar '0'
    soma, calculo = 0, 0  # Serão usados para pegar o penultimo e ultimo numero do CPF.
    numeros_do_cpf, cpf_copia = [], []

    linha(vezes=18)
    try:
        cpf = str(input('Digite o CPF: ')).strip()
    except:
        erro('Por favor\ndigite o CPF corretamente.')
    else:
        if len(cpf) == 1 and cpf == '0':  # Se o usuario decidir encerrar o programa.
            break

        if len(cpf) == 14 or len(cpf) == 11 and cpf.isalpha() == False:  # Se for do tamanho de um CPF.

            for n in cpf:  # Pegando somente os numeros do CPF.
                if n.isdigit():
                    numeros_do_cpf.append(int(n))

            for p, n in enumerate(range(10, 1, -1)):  # Pegando a multiplicacao de cada numero na sequencia que foi mostrada na aula e fazendo a soma.
                soma += numeros_do_cpf[p] * n

            calculo = 11 - (soma % 11)
            calculo = 0 if calculo > 9 else calculo
            cpf_copia.append(numeros_do_cpf[:9])
            cpf_copia.append(calculo)

            calculo, soma = 0, 0  # Zerando as variaveis para pegar o calculo do ultimo numero do CPF.

            for p, n in enumerate(range(11, 1, -1)):
                soma += numeros_do_cpf[p] * n

            calculo = 11 - (soma % 11)
            calculo = 0 if calculo > 9 else calculo
            cpf_copia.append(calculo)

            print(f'\nO CPF ({cpf}) é \033[;32mvalido\033[m' if cpf_copia[-2:] == numeros_do_cpf[-2:] else f'\nO CPF ({cpf}) é \033[;31minvalido\033[m')

        else:
            erro('Por favor\ndigite o CPF corretamente.')

programa_encerrado()
