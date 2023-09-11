import re

while True:  # Enquanto o usuario nao digitar corretamente o CPF

    cpf = str(input('Informe o CPF: '))

    formato_cpf = re.findall(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf)  # Pegando o formato exato do CPF
    formato2_cpf = re.findall(r'\d{11}', cpf)

    if len(formato_cpf) >= 1 or len(formato2_cpf) >= 1:  # Se o formato do CPF estiver correto.
        numeros_do_cpf = re.findall(r'\d', cpf)
        numeros_do_cpf = ''.join(numeros_do_cpf)

        if len(numeros_do_cpf) == 11:  # Se a quantidade de caracteres do CPF for o padrao.

            cpf_clone = numeros_do_cpf[:9]  # Pegando os numeros do CPF, menos os 2 ultimos

            for c in range(2):  # Fazendo o calculo para validar o CPF
                if c == 0:  # Fazendo calculo para pegar o penultimo digito do CPF
                    soma = 0
                    for index, cont in enumerate(range(10, 1, -1)):
                        soma += int(numeros_do_cpf[index]) * cont

                    calculo = 11 - (soma % 11)
                    calculo = 0 if calculo > 9 else calculo
                    cpf_clone += str(calculo)

                else:  # Fazendo calculo para pegar o ultimo digito do CPF
                    soma = 0
                    for index, cont in enumerate(range(11, 1, -1)):
                        soma += int(numeros_do_cpf[index]) * cont

                    calculo = 11 - (soma % 11)
                    calculo = 0 if calculo > 9 else calculo
                    cpf_clone += str(calculo)

            if cpf_clone == numeros_do_cpf:  # Se a validacao do CPF estiver valida.
                print('\n\n\t\tEste CPF é valido\n\n')
                break

            else:
                print('\n\n\t\tEste CPF é invalido\n\n')
                break

        else:  # Se o usuario nao digitou o formato do CPF corretamente.
            print('\n\n\t\t[ERRO]: Informe o formato do CPF corretamente.\n\n')

    else:
        print('\n\n\t\t[ERRO]: Informe o formato do CPF corretamente.\n\n')
