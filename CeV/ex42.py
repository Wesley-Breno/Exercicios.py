# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

from functions import titulo, press_enter, erro, pular, encerrar, programa_encerrado    # Funcoes que criei.

deseja = 0    # Variavel para saber se o usario deseja encerrar o programa, recebe 0 se nao, recebe 1 se sim.

titulo('▴ Triangulos ▴')
press_enter()

while deseja != 1:    # Enquanto o usuario nao desejar encerrar o programa.
    try:    # Pegando os lados do triangulo.
        lado1 = int(input('\n\nInforme o valor do 1° lado: '))
        lado2 = int(input('Informe o valor do 2° lado: '))
        lado3 = int(input('Informe o valor do 3° lado: '))
    except:    # Mensagem de erro, caso dê algo de errado.
        erro('Por favor\nVerifique os dados inseridos.')
        pular(5)
    else:
        if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:    # Se os valores informados, formarem um triangulo.
            print('\n\nOs valores formam um triangulo: ', end='')
            if lado1 == lado2 == lado3 == lado1:    # Se os valores formam um triangulo equilatero.
                print('Equilatero')
            elif lado1 != lado2 != lado3 != lado1:    # Se os valores formam um triangulo escaleno.
                print('Escaleno')
            else:    # Se os valores formam um triangulo isosceles.
                print('Isosceles')
        else:
            print('\nOs valores informados nao formam um triangulo.')

        pular()
        print('__' * 16)
        press_enter('para continuar.')
        deseja = encerrar()    # Perguntando ao usuario se deseja encerrar o programa.
        if deseja == 0:    # Se o usuario nao quiser encerrar, o programa ira pular 5 linhas.
            pular(5)

programa_encerrado()    # Mensagem de despedida para o usuario.
