# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.

from functions import titulo, erro, pular, encerrar, press_enter, programa_encerrado

deseja = 0  # Variavel para saber se o usuario deseja encerrar
while deseja != 1:  # Enquanto deseja nao for igual a 1 o codigo ira ficar no loop
    titulo('Digitos separados')
    try:
        numero = int(input('Digite um valor de 0 a 9999\nNumero:  '))
    except:
        erro('Digite um valor valido.')
    else:
        if numero < 0 or numero > 9999:     # Se o numero for menor que zero ou maior que 9999
            erro('Digite um valor de 0 a 9999.')
        else:
            cont = 0    # Variavel para contar o total de numeros que tem no valor
            numero_str = str(numero)    # Variavel com o valor convertido para string para pegar a unidade e etc.
            for n in numero_str:
                cont += 1

            if cont == 1:   # Se o valor so tiver unidade
                pular(3)
                print('__' * 16)
                print(f'''Unidade: \t{numero_str[-1]}
Dezena: \tNull
Centena: \tNull
Milzena: \tNull

Valor que foi analisado: {numero}''')
                print('__' * 16)
                press_enter()
                deseja = encerrar()
                pular(5)

            elif cont == 2:     # Se o valor so tiver dezena
                pular(3)
                print('__' * 16)
                print(f'''Unidade: \t{numero_str[-1]}
Dezena: \t{numero_str[-2]}
Centena: \tNull
Milzena: \tNull

Valor que foi analisado: {numero}''')
                print('__' * 16)
                press_enter()
                deseja = encerrar()
                pular(5)

            elif cont == 3:     # Se o valor so tiver milzena
                pular(3)
                print('__' * 16)
                print(f'''Unidade: \t{numero_str[-1]}
Dezena: \t{numero_str[-2]}
Centena: \t{numero_str[-3]}
Milzena: \tNull

Valor que foi analisado: {numero}''')
                print('__' * 16)
                press_enter()
                deseja = encerrar()
                pular(5)

            else:   # Se o valor estiver com todos os 4 numeros (Milzena)
                pular(3)
                print('__' * 16)
                print(f'''Unidade: \t{numero_str[-1]}
Dezena: \t{numero_str[-2]}
Centena: \t{numero_str[-3]}
Milzena: \t{numero_str[-4]}

Valor que foi analisado: {numero}''')
                print('__' * 16)
                press_enter()
                deseja = encerrar()
                pular(5)

programa_encerrado()    # Funçao para mostrar uma mensagem de adeus quando o programa for encerrado
