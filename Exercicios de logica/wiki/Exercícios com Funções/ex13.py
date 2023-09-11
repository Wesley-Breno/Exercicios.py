"""
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o
valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de
forma elegante.
"""


def desenha_retangulo(x=10, y=10):
    """
    Funcao que desenha um retangulo.
    se os parametros da altura e largura nao forem informados, o programa ira deixar os parametros com o valor 10.
    :param x:  Largura do retangulo
    :param y:  Altura do retangulo
    :return:   None
    """
    sinais = ['+', '-', '|']

    while True:  # Enquanto o programa nao desenhar o retangulo
        if x >= y:  # Se a largura for maior ou igual a altura

            # Desenhando largura da parte de cima
            cont_sinal = 0  # Variavel que sera usada para chamar os sinais por seus indices
            for c in range(x):
                print(sinais[cont_sinal], end='')
                cont_sinal += 1
                if cont_sinal > 2:  # Se chegou no ultimo indice dos sinais
                    cont_sinal = 0  # Volta ao primeiro sinal
            print()

            # Desenhando cada linha ate ter a altura especificada
            for c in range(y):
                print(sinais[cont_sinal], end='')
                cont_sinal += 1
                if cont_sinal > 2:
                    cont_sinal = 0
                for espaco in range(x - 2):  # Desenhando espacos do meio do retangulo
                    print(' ', end='')
                print(sinais[cont_sinal], end='')
                cont_sinal += 1
                if cont_sinal > 2:
                    cont_sinal = 0
                print()

            # Desenhando largura da parte de baixo
            for c in range(x):
                print(sinais[cont_sinal], end='')
                cont_sinal += 1
                if cont_sinal > 2:
                    cont_sinal = 0

            break

        else:  # Se a largura e a altura nao tiverem o valor necessario
            x = 10
            y = 10


if __name__ == '__main__':
    desenha_retangulo()
