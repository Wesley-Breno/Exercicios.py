# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

from functions import erro

parar = 0
while True:
    if parar == 1:
        break
    else:
        print(f'\n\033[;1m{"_- Medidor de tinta -_":^45}\033[m\n')

        try:
            largura = float(input('\nDigite a largura da parede: '))
            altura = float(input('Digite a altura da parede: '))
        except:
            erro()
        else:
            area = largura * altura
            tinta_necessaria = (largura * altura) / 2
            print(f'\nVoce precisara de \033[;1m{tinta_necessaria}\033[ml de tinta\nPara pintar a area da sua parede de {area}m².')
            while True:
                try:
                    encerrar = str(input('\nDeseja encerrar o programa?\n[S]/[N] -> ')).upper()[0]
                except:
                    erro('Digite [S] para Sim.\nDigite [N] para Não.')
                else:
                    if encerrar == 'S':
                        print(f'\n\n{"_- Programa encerrado com sucesso -_":^45}')
                        print(f'{"_- Ate logo -_":^45}\n\n')
                        parar += 1
                        break
                    elif encerrar == 'N':
                        parar = 0
                        break
                    else:
                        erro('Digite [S] para Sim.\nDigite [N] para Não.')
