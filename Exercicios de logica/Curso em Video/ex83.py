"""
Crie um programa onde o usuário digite uma expressão qualquer que use
parênteses. Seu aplicativo deverá analisar se a expressão passada está
com os parênteses abertos e fechados na ordem correta.
"""

parenteses_abertos, parenteses_fechados = 0, 0  # Variaveis onde ficaram a contagem de expressoes iniciadas/finalizadas

print('__' * 16)
expressao = str(input('Digite a expressao numerica: '))

if len(expressao) > 0:
    for caractere in expressao:

        if caractere == '(':  # Se tiver iniciado uma expressao
            parenteses_abertos += 1

        if caractere == ')':  # Se tiver finalizado uma expressao
            parenteses_fechados += 1

    if parenteses_abertos == 0 and parenteses_fechados == 0:  # Se nao foi digitado nenhuma expressao
        print('\n\n\t\tVoce nao digitou nenhuma expressao\n\n')

    else:
        if parenteses_abertos == parenteses_fechados:  # Se a contagem de expressoes abertas for a mesma das fechadas
            print('\n\n\t\tSua expressao esta \033[;32mcorreta\033[m.\n\n')

        elif parenteses_abertos > parenteses_fechados:  # Se o usuario nao fechou alguma expressao
            print('\n\n\t\t[\033[;31mERRO\033[m]: Feche as expressoes\n\n')

        else:  # Se ele fechou alguma expressao sem ter iniciado uma
            print('\n\n\t\t[\033[;31mERRO\033[m]: Inicie a expressao antes de fecha-la\n\n')

else:
    print('\n\n\t\t[\033[;31mERRO\033[m]: Voce nao digitou nada\n\n')
