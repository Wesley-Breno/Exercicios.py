# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

from functions import titulo, press_enter, erro, pular, programa_encerrado    # Funcoes que criei.

titulo('IMC')
press_enter()

while True:    # Enquanto o usuario nao digitar 0.
    print(f'\n\n\033[;37m{"Digite [ 0 ] para encerrar.":^45}\033[m')

    try:
        peso = float(input('\nInforme o peso em KGs: '))
        if peso == 0:    # Se o usuario digitar 0, o programa sera encerrado.
            break
        altura = float(input('Informe a altura: '))
        if altura == 0:    # Se o usuario digitar 0, o programa sera encerrado.
            break
    except:
        erro('Por favor\nverifique os valores informados.')
        pular(5)
    else:
        imc = peso / (altura * altura)    # Calculo para saber o IMC.

        pular(3)
        print('▰▰' * 15)
        print('Voce esta ', end='')

        if imc < 18.5:
            print('\033[1;31mabaixo\033[m do peso.')
        elif 18.5 <= imc < 25:
            print('no peso \033[1;32mideal\033[m.')
        elif 25 <= imc < 30:
            print('no \033[1;33msobrepeso\033[m.')
        elif 30 <= imc < 40:
            print('na \033[1;31mobesidade\033[m.')
        else:
            print('na \033[1;31mOBESIDADE MORBIDA\033[m.')

        print(f'Seu IMC é \033[;1m{imc:.1f}\033[m')
        print('▰▰' * 15)
        press_enter('para calcular de novo.')
        pular(5)

programa_encerrado()    # Mensagem de despedida para o usuario.
