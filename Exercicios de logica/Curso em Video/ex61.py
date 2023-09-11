"""
Refaça o DESAFIO 051
lendo o primeiro termo e a razão de uma PA
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
while True:  # Enquanto o usuario nao digitar o valor do termo e razao corretamente.
    try:
        termo = int(input('Termo > '))
        razao = int(input('Razao > '))
    except:
        print('\n\t\t\033[1;31mERRO\033[m, digite os valores corretamente\n')
    else:
        calculo = 0  # Variavel de mudanca constante de valor para mostrar cada termo da PA
        cont = 0  # Contador para mostrar apenas os 10 primeiros termos

        print('\n\t\t\t10 termos da PA')
        while cont != 10:
            # Se for o primeiro termo, ira receber ele mesmo. Se nao for, ira receber a razao.
            calculo = calculo + termo if cont == 0 else calculo + razao
            if cont < 9:
                print(calculo, end=' > ')
            else:
                print(calculo)
            cont += 1

        break
