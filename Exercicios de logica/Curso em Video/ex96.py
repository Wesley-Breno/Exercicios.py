"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento_informado) e mostre a área do terreno.
"""


def area(largura: float, comprimento: float):
    """
    Funcao para calcular uma area informada com base nos parametros.

    :param largura: Parametro onde recebera um valor float para ser a largura.
    :param comprimento: Parametro onde recebera um valor float para ser o comprimento
    :return:Retorna o valor da area com base nos valores informados.
    """
    return largura * comprimento


print('\n\t\tComprimento do terreno')
print('--' * 20)

while True:  # Enquanto o usuario nao digitar os valores corretamente.
    try:
        largura_informada = float(input('Digite a largura da area (m): '))
        comprimento_informado = float(input('Digite o comprimento_informado da area (m): '))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe os valores [Largura, Comprimento] com valores reais.\n\n')

    else:
        resultado_area = area(largura_informada, comprimento_informado)  # Pegando o valor da area
        break

print(f'\n\t\tA area de um terreno {largura_informada}x{comprimento_informado} é de {resultado_area}m².\n')
