# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

from functions import titulo, erro, pular, press_enter, encerrar, programa_encerrado

titulo('Numero maior e menor')

deseja = 0  # Variavel para saber se o usuario quer encerrar o programa.

while deseja != 1:  # Enquanto o usuario nao desejar encerrar o programa.
    try:    # Tentando pegar os 3 numeros, caso contrario, aparecera um erro.
        numeros = [int(input(f'Digite o {n + 1}° numero: ')) for n in range(3)]
    except:
        erro('Por favor\n\nTente novamente e coloque\num valor valido.')
        pular(5)
    else:
        maior, menor, contador = 0, 0, 0    # Variaveis do maior numero, menor numero e o contador.

        for n in numeros:
            if contador == 0:   # Se for a primeira vez que o loop for é iniciado, o menor numero ira receber ele mesmo.
                menor = n
            else:
                if n < menor:   # Se o numero da vez for menor que o numero que esta na variavel 'menor'.
                    menor = n
            if n > maior:   # Se o numero da vez for maior que o numero que esta na variavel 'maior'.
                maior = n
            contador += 1

        print(f'\nMaior numero > {maior}\nMenor numero > {menor}\n')
        press_enter()

        deseja = encerrar()  # Perguntando se o usuario deseja encerrar. 1 para sim, 0 para nao.
        if deseja == 0:
            pular(5)

programa_encerrado()
