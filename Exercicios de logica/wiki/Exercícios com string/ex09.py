"""
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
"""

import re


def valida_cpf(cpf_informado: str) -> bool:
    """
    Funcao responsavel por receber a string ou numero de um cpf, validar seu formato e apos isso a funcao cria um copia
    do cpf sem o penultimo e ultimo digito, para assim fazer o calculo para gerar esses dois ultimos digitos e comparar
    com o cpf original. Caso a copia do cpf com os ultimos digitos gerados pelo calculo forem iguais aos do cpf original
    esse cpf é valido. Caso contrario, é invalido.
    :param cpf_informado: String ou valor numerico recebido que deve ser um cpf
    :return: Retorna True se o formato do cpf estiver correto e o seu calculo tambem. Caso contrario, retornar False.
    """
    try:
        cpf = re.match(r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$', cpf_informado)[0]  # Verificando se o formato é de um cpf

    except TypeError:
        return False

    else:
        # Se o formato do parametro informado for de um cpf
        if len(cpf) == 14 or len(cpf) == 11 and cpf.isalpha() is False:

            numeros_do_cpf, cpf_copia = [], []

            # Pegando somente os numeros do CPF.
            for n in cpf:
                if n.isdigit():
                    numeros_do_cpf.append(int(n))

            cpf_copia.append(numeros_do_cpf[:9])  # Criando copia do cpf mas sem os 2 ultimos digitos

            # Calculando e adicionanodo os 2 ultimos digitos com base no calculo de verificacao
            for index_penultimo_e_ultimo in range(10, 12):
                calculo, soma = 0, 0

                for p, n in enumerate(range(index_penultimo_e_ultimo, 1, -1)):  # Pegando a multiplicacao de cada numero
                    soma += numeros_do_cpf[p] * n

                calculo = 11 - (soma % 11)
                calculo = 0 if calculo > 9 else calculo
                cpf_copia.append(calculo)

            if cpf_copia[-2:] == numeros_do_cpf[-2:]:  # Os dois ultimos digitos calculados forem iguais ao cpf original
                return True

            return False

        else:
            return False


cpf_usuario = str(input('Informe um CPF no formato xxx.xxx.xxx-xx: '))
valido = valida_cpf(cpf_usuario)

if valido:
    print(f'\n\n\t\tO CPF {cpf_usuario} é valido')
else:
    print(f'\n\n\t\tO CPF {cpf_usuario} é invalido')
