# Valide um CPF

# Funcoes que minhas que foram usadas
from functions import erro, titulo, press_enter, encerrar, programa_encerrado, pular

deseja = 0  # Variavel usada para saber se o usuario quer encerrar
while deseja != 1:
    titulo('Validador de CPFs')
    try:
        cpf = str(input('\nInforme o CPF: '))
    except:
        erro('Digite o CPF apenas com\nos numeros.')
    else:
        if cpf.isnumeric():     # Se o cpf estiver somente em numeros
            if len(cpf) == 11:  # Se o cpf tiver 11 caracteres
                contador_decrescente = 10
                soma1, soma2, numero1, numero2 = 0, 0, 0, 0
                # Operacao para calcular o penultimo numero do CPF
                for n in cpf[:9]:
                    soma1 += int(n) * contador_decrescente
                    contador_decrescente -= 1
                resultado1 = 11 - (soma1 % 11)
                if resultado1 > 9:
                    numero1 = 0
                else:
                    numero1 = resultado1
                # Operacao para calcular o ultimo numero do CPF
                print()
                contador_decrescente = 11
                for n in cpf[:9]:
                    soma2 += int(n) * contador_decrescente
                    contador_decrescente -= 1
                    if contador_decrescente == 2:
                        soma2 += numero1 * contador_decrescente
                resultado2 = 11 - (soma2 % 11)
                if resultado2 > 9:
                    numero2 = 0
                else:
                    numero2 = resultado2
                # Criando um novo cpf com os calculos que foram feitos
                novo_cpf = []
                for n in cpf[:9]:
                    novo_cpf.append(n)
                novo_cpf.append(str(numero1))
                novo_cpf.append(str(numero2))
                novo_cpf = ''.join(novo_cpf)
                # Se o novo cpf for igual ao antigo entao o cpf é valido
                if cpf == novo_cpf:
                    print('\nEste CPF é \033[1;32mvalido\033[m')
                else:
                    print('\nEste CPF é \033[1;31minvalido\033[m')
                press_enter()
                deseja = encerrar()     # Pergunta se o usuario deseja encerrar o programa
                if deseja == 0:     # Se o usuario nao decidir encerrar o programa ira pular 5 linhas
                    pular(5)
            else:
                erro('O CPF deve conter 11 numeros.')
        else:
            erro('Digite o CPF apenas com\nos numeros.')

programa_encerrado()
