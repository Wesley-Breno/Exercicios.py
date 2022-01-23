"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor lista.

Exemplo:

    lista_a     = [1, 2, 3, 4, 5, 6, 7]
    lista_b     = [1, 2, 3, 4]
===================
resultado

    lista_soma  = [2, 4, 6, 8]
"""

from functions import titulo, press_enter, erro, pular, encerrar, programa_encerrado

deseja = 0  # Variavel que tera a resposta se o usuario quer encerrar o programa ou nao.

while deseja != 1:  # Enquanto a resposta do usuario for difente de 1 o programa continuara.

    lista_a = []    # Lista A e B onde ficarao os numeros colocados pelo usuario.
    lista_b = []
    soma_das_listas = []    # Lista onde ira ficar a soma de cada numero das listas.

    titulo('Somando duas listas')
    press_enter('para começar.')
    print(f'\n\n\033[1;37m{"-- Digite 0 para adicionar na outra lista --":^55}\033[m\n')

    while True:  # Adicionando numeros para a lista_A.
        try:
            numero_lista_a = int(input('Adicionar numero: '))
        except:
            erro('Por favor\n\nVerifique o dado que foi\ninserido.')
            pular(5)
        else:
            if numero_lista_a == 0:  # Se o usuario digitar 0, ira começar a adicionar numeros na lista_B.
                break
            else:
                lista_a.append(numero_lista_a)

    print(f'\n\n\033[1;37m{"-- Digite 0 para mostrar a soma --":^45}\033[m\n')

    while True:  # Adicionando numeros a lista_B.
        try:
            numero_lista_b = int(input('Adicionar numero: '))
        except:
            erro('Por favor\n\nVerifique o dado que foi\ninserido.')
            pular(5)
        else:
            if numero_lista_b == 0:  # Se o usuario digitar 0, ira mostrar a soma dos numeros.
                break
            else:
                lista_b.append(numero_lista_b)

    listas_juntas = zip(lista_a, lista_b)   # Pegando cada numero de cada lista.
    for a, b in listas_juntas:  # Somando cada numero e adicionando na lista 'soma_das_listas'.
        soma_das_listas.append(a + b)

    print(f'\n\n\n\033[1;37m{"Somando cada valor de cada lista":^45}\033[m')
    print(f'''
Lista A: {lista_a}
Lista B: {lista_b}
          ⇅
Somados: {soma_das_listas}\n''')
    press_enter()

    deseja = encerrar()  # Perguntando se o usuario quer encerrar o programa. Se sim a variavel 'deseja' vai receber 1.
    if deseja == 0:  # Se o usuario nao quiser encerrar o programa, o programa ira pular 10 linhas.
        pular(10)

programa_encerrado()    # Mensagem de despedida depois de encerrar o programa.
