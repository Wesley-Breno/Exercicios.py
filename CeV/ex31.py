# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

from functions import titulo, press_enter, erro, programa_encerrado, pular

titulo('Valor da passagem')
press_enter('para calcular sua passagem.')

while True:
    try:
        print(f'\n\n\033[;37m{"Digite 0 para encerrar o programa":^45}\033[m\n\n')
        km = float(input('Digite a distancia total da viagem em KMs...\nKm: '))    # KMs da viagem
    except:
        erro('Por favor\nVerifique os dados informados.')
        pular(5)
    else:
        if km == 0:    # Se o usuario digitar 0 o programa sera encerrado
            break
        else:
            if km > 200:    # Se a viagem for mais de 200KMs, o preco por cada Km é R$00.45
                valor = km * 0.45
            else:    # Se for menos ou igual a 200KMs, o preco por cada Km é R$00.50
                valor = km * 0.50

            pular(5)
            print('__' * 17)
            print(f'{f"Total de KMs > {int(km)}"}\n{f"Preco da passagem > R${valor:.2f}"}')
            print('__' * 17)
            press_enter('para fazer outro calculo.')
            pular(5)

programa_encerrado()
