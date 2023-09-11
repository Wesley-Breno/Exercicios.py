# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

from functions import titulo, press_enter, erro, linha, pular, programa_encerrado    # Funcoes que criei

encerrar = 0    # Variavel que vai receber 1, se o usuario quiser encerrar.

titulo('Maior e menor peso')
press_enter('para comecar.')

while encerrar <= 0:    # Enquanto o usuario nao quiser encerrar.

    pesos = []
    maior, menor, cont, valor, encerrar = 0, 0, 0, 0, 0

    pular(3)
    print(f'\033[;37m  Digite [ 0 ] para encerrar\033[m')
    linha('__', 15)
    try:
        for c in range(0, 5):
            valor = float(input(f'Informe o {c + 1}° peso: '))

            if valor == 0:    # Se o usuario digitou 0 para encerrar.
                encerrar += 1
                break
            else:
                pesos.append(valor)

    except:
        erro('Informe o peso corretamente'
             '\nusando ( . ) para os numeros decimais.')
    else:
        if encerrar > 0:    # Se 'encerrar' for maior que 0, o programa é encerrado.
            linha('__', 15)
            break

        for p in pesos:
            if cont == 0:    # Se for a primeira vez que estiver comparando os pesos.
                maior = p
                menor = p
                cont += 1
            else:
                if p > maior:
                    maior = p
                if p < menor:
                    menor = p

        linha('__', 14)
        print(f'Maior peso: {maior}\nMenor peso: {menor}')
        linha('__', 14)
        press_enter()
        pular(5)

programa_encerrado()
