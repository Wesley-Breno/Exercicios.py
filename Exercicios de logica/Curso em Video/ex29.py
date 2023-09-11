# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

from functions import titulo, press_enter, pular, programa_encerrado, erro

while True:
    titulo('Detranzinho')
    print(f'\033[;37m{"Digite 0 para encerrar":^45}\033[m')
    try:    # velocidade do carro.
        velocidade = float(input('\n\nInforme quantos Kilometros p/ hora o carro estava...\nKM/h: '))
    except:    # Mostrara um erro se o usuario nao digitar um dado valido.
        erro('Por favor\nInforme um dado valido.')
    else:
        if velocidade == 0:    # Se o usuario digitar 0 o programa ira encerrar.
            break
        if velocidade > 80:    # Se a velocidade passar de 80Kmh ira ser feito o calculo.
            multa = (velocidade - 80) * 7    # Cada km ira ser multiplicado por 7 que por fim sera o valor da multa.
            print(f'\n\n{"Voce ultrapassou o limite de velocidade de 80Km/h":^45}')
            print(f'{f"Sua multa sera de R${multa:.2f}":^45}\n\n')
            press_enter('para voltar a tela inicial.')
            pular(10)
        else:
            print(f'\n\n{"Voce esta dentro do limite de velocidade":^45}')
            print(f'{"Continue assim :)":^45}\n\n')
            press_enter('para voltar a tela inicial.')
            pular(10)

pular(10)
programa_encerrado()
