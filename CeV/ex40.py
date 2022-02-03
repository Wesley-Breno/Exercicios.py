# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO


from functions import titulo, press_enter, pular, erro, encerrar, programa_encerrado    # FUncoes que criei.

deseja = 0    # Recebe 1 se o usuario deseja encerrar, recebe 0 se nao quiser encerrar.

titulo('Calculador de media')

while deseja != 1:     # Enquanto o usuario nao desejar encerrar o programa.
    try:    # Tentando pegar as duas notas.
        nota1 = float(input('\nDigite a 1° nota: '))
        nota2 = float(input('Digite a 2° nota: '))
    except:    # Mensagem de erro, caso o usuario colocar um dado invalido.
        erro('Por favor\nVerifique os dados inseridos.')
        pular(5)
    else:
        media = (nota1 + nota2) / 2    # Pegando a media das duas notas.

        pular(5)
        print('--' * 25)
        print(f'Notas \033[;1m>\033[m {nota1:.1f}, {nota2:.1f}')
        print(f'Media \033[;1m>\033[m {media:.1f}')

        if media < 5.0:    # Se o aluno tirar uma nota menor que 5.0, ele é reprovado.
            print(f'\n\033[1;31m{"Reprovado":^45}\033[m')
        elif media <= 6.9:    # Se o aluno tirar uma nota entre 5.0 e 6.9, ele estara na recuperacao.
            print(f'\n\033[1;33m{"Recuperacao":^45}\033[m')
        else:    # Se o aluno tirar uma nota maior que 6.9, ele estara aprovado.
            print(f'\n\033[1;32m{"Aprovado":^45}\033[m')

        print('--' * 25)
        press_enter()

        deseja = encerrar()    # Perguntando ao usuario se ele quer encerrar o programa.
        if deseja == 0:    # Se o usuario nao quiser encerrar o programa, o programa ira pular 5 linhas.
            pular(5)

programa_encerrado()    # Mensagem de despedida apos o usuario decidir encerrar o programa.
