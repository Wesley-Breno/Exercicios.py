# Faça um gerador de CPFs

# Funcoes minhas que foram usadas
from functions import titulo, press_enter, encerrar, programa_encerrado, pular
from random import randint  # Usado para gerar numeros inteiros aleatorios

deseja = 0  # Variavel usada para saber se o usuario quer encerrar
while deseja != 1:
    titulo('Gerador de CPFs')
    press_enter('para gerar um CPF.')

    contador_decrescente = 10  # diminui ate 0 para parar de multiplicar
    soma1, soma2, numero1, numero2 = 0, 0, 0, 0  # A soma dos 2 calculos e os 2 ultimos digitos do novo CPF

    # Criando uma variavel CPF que vai receber 11 caracteres
    cpf = []
    for c in range(0, 11):
        cpf.append(str(randint(0, 9)))
    cpf = ''.join(cpf)

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
        pular(3)
        print('__' * 12)
        print(f'Aqui esta seu CPF↴\n\n\033[;1m{cpf:^26}\033[m')   # Mostrando o CPF valido ao usuario
        print('__' * 12)

    # Se o algoritmo nao conseguir achar um CPF valido de primeira...
    else:
        while cpf != novo_cpf:  # Enquanto o algoritmo nao criar um CPF que seja valido ele ira ficar no loop

            contador_decrescente = 10   # diminui ate 0 para parar de multiplicar
            soma1, soma2, numero1, numero2 = 0, 0, 0, 0  # A soma dos 2 calculos e os 2 ultimos digitos do novo CPF

            # Criando uma variavel CPF que vai receber 11 caracteres
            cpf = []
            for c in range(0, 11):
                cpf.append(str(randint(0, 9)))
            cpf = ''.join(cpf)

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
                pular(3)
                print('__' * 12)
                print(f'Aqui esta seu CPF↴\n\n\033[;1m{cpf:^26}\033[m')
                print('__' * 12)
                break

    press_enter()
    deseja = encerrar()     # Pergunta se o usuario deseja encerrar o programa
    if deseja == 0:     # Se o usuario nao decidir encerrar o programa ira pular 5 linhas
        pular(5)

programa_encerrado()
