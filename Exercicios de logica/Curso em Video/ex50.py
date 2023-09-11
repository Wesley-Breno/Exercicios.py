# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

from functions import titulo, press_enter, programa_encerrado, pular, erro    # Funcoes que criei.

deseja = 0    # Variavel para saber se o usuario deseja encerrar o programa. Recebe 1 para sim, 0 para nao.

titulo('Soma dos pares')
press_enter('para comecar.')

while deseja == 0:    # Enquanto o usuario quiser continuar o programa.
    lista_pares = []    # Lista onde ficara todos os numeros pares que foram digitados.
    soma = 0    # Variavel onde ficara a soma dos numeros pares.

    print(f'\n\n\033[;37m{"Digite [ 0 ] para encerrar.":^45}\033[m\n')

    for c in range(0, 6):    # Fazendo um for de 0 a 6 para pegar os 6 numeros.
        try:
            num = int(input(f'Digite o {c + 1} numero: '))
        except:
            erro('Por favor\nInforme um valor valido.')
            break
        else:
            if num == 0:    # Se o numero for zero, o programa ira encerrar.
                deseja += 1
                break
            if num % 2 == 0:    # Se o numero for divisivel por 2, coloque ele na lista de pares.
                lista_pares.append(num)
                soma += num

    if deseja > 0:    # Se o usuario desejou encerrar.
        break
    else:
        print(f'\n\n\033[;1m{"Resultado":^45}\033[m')

        if len(lista_pares) == 0:    # Se o usuario nao digitou nenhum numero par.
            print(f'\n\n{"Voce nao digitou nenhum numero par":^45}\n\n')
        else:
            if len(lista_pares) == 1:    # Se o usuario digitou so um numero par.
                print(f'\n\n\t\tVoce so digitou um numero par'
                      f'\n\t\tNao tem como fazer uma soma.'
                      f'\n\t\tNumero par digitado: {lista_pares}\n\n')
            else:
                print(f'\n\n\t\tValores pares recolhidos: {lista_pares}'
                      f'\n\t\tSoma dos valores pares: {soma}\n\n')

        press_enter('para colocar novos numeros.')
        pular(4)

programa_encerrado()
