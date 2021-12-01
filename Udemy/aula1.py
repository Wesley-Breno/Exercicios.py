from time import localtime  # Metodo para pegar o tempo atual

while True:
    print(f'\n\033[;1m{"Bem vindo ao menu":^45}\033[m')
    try:
        escolha = int(input('''\nDigite o numero que corresponde\na escolha que deseja fazer.


1 \033[1;31m➣\033[m Exercicio 1.

2 \033[1;31m➣\033[m Exercicio 2.

3 \033[1;31m➣\033[m Exercicio 3.

4 \033[1;31m➣\033[m Informações.

0 \033[1;31m➣\033[m Encerrar.


Escolha: '''))
    except:
        print('\n\033[1;31mERRO\033[m\nVerifique o valor inserido.\nPor favor, tente novamente.')
        print()
        print('__' * 18)
        input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
        print('\n' * 5)
    else:
        if escolha == 1:
            print(f'\n\n{"Exercicio 1":^45}')
            try:
                numero = int(input('\nDigite um numero inteiro: '))
            except:
                print('\n\033[1;31mERRO\033[m\nInfelizmente, voce nao digitou um numero inteiro.\nPor favor, tente novamente.')
                print()
                print('__' * 18)
                input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
                print('\n' * 5)
            else:
                if type(numero) != int:
                    print('\n\033[1;31mERRO\033[m\nInfelizmente, voce nao digitou um numero inteiro.\nPor favor, tente novamente.')
                    print()
                    print('__' * 18)
                    input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
                    print('\n' * 5)
                else:
                    if numero % 2 == 0:
                        print(f'\nO numero {numero} é um numero \033[1;32mpar\033[m.')
                        print()
                        print('__' * 18)
                        input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
                        print('\n' * 5)
                    else:
                        print(f'\nO numero {numero} é um numero \033[1;31mimpar\033[m.')
                        print()
                        print('__' * 18)
                        input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
                        print('\n' * 5)
        elif escolha == 2:
            print(f'\n\n{"Exercicio 2":^45}')
            hora = localtime()[3:5]  # Hora atual
            if hora[0] <= 11:
                print(f'\n\n{f"São exatamente {hora[0]}:{hora[1]}":^45}')
                print(f'{"Bom dia ❤":^45}')
            elif hora[0] <= 17:
                print(f'\n\n{f"São exatamente {hora[0]}:{hora[1]}":^45}')
                print(f'{"Boa tarde ❤":^45}')
            elif hora[0] <= 23 or hora[0] == 24 or hora[0] == 0:
                print(f'\n\n{f"São exatamente {hora[0]}:{hora[1]}":^45}')
                print(f'{"Boa noite ❤":^45}')
            print()
            print('__' * 18)
            input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
            print('\n' * 5)
        elif escolha == 3:
            print(f'\n\n{"Exercicio 3":^45}')
            try:
                nome = str(input('\n\nPor favor, digite o seu 1º nome abaixo...\nNome: ').strip().title())
            except:
                print('\n\n\033[1;31mERRO\033[m\nVerifique o valor inserido.\nPor favor, tente novamente.')
                print()
                print('__' * 18)
                input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
                print('\n' * 5)
            else:
                # Pegando o primeiro nome e verificando se tem numero/caracte especial.
                nome_lista = nome.split()
                if nome_lista[0].isalpha():
                    total_de_caracteres = len(nome_lista[0])
                    if total_de_caracteres <= 4:
                        print(f'''\n\nSeu nome é curto

Nome: {nome_lista[0]}
Total de caracteres: {total_de_caracteres}''')
                        print()
                        print('__' * 18)
                        input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
                        print('\n' * 5)
                    elif total_de_caracteres <= 6:
                        print(f'''\n\nSeu nome tem um tamanho normal

Nome: {nome_lista[0]}
Total de caracteres: {total_de_caracteres}''')
                        print()
                        print('__' * 18)
                        input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
                        print('\n' * 5)
                    elif total_de_caracteres > 6:
                        print(f'''\n\nSeu nome é muito grande

Nome: {nome_lista[0]}
Total de caracteres: {total_de_caracteres}''')
                        print()
                        print('__' * 18)
                        input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
                        print('\n' * 5)
                else:
                    if nome == '':
                        print(f'\n\033[1;31mERRO\033[m\nDigite um nome valido.\nPor favor, tente novamente.')
                        print()
                        print('__' * 18)
                        input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
                        print('\n' * 5)
                    else:
                        print(f'\n\033[1;31mERRO\033[m\n\n[ {nome_lista[0]} ]\nNao use numeros e caracteres especiais\nPor favor, tente novamente.')
                        print()
                        print('__' * 18)
                        input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
                        print('\n' * 5)
        elif escolha == 4:
            print('\n' * 5)
            print(f'\033[1;37m{"Informações":^65}\033[m')
            print('''
    Neste software feito por mim, deixei 3 exercicios que foram
    feitos no curso do \033[;1m@otaviomirandabr\033[m na plataforma Udemy.
    (Os exercicios so foram feitos apenas para o meu aprendizado na linguagem.)
    
    Exercicio 1
        Faça um programa que peça ao usuario para digitar um numero inteiro,
        informe se este numero é par ou impar. Caso o usuario não digite um
        numero inteiro, informe que não é um numero inteiro.
    
    Exercicio 2
        Faça um programa que pergunte a hora ao usuario e, baseando-se no ho-
        rario descrito, exiba a saudação apropriada. EX.
        Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
        
    Exercicio 3
        Faça um programa que peça o primeiro nome do usuario. Se o nome tiver
        4 letras ou menos, escreva "Seu nome é  curto"; se tiver entre 5 e 6
        letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é
        muito grande".''')
            print()
            print('__' * 18)
            input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
            print('\n' * 5)
        elif escolha == 0:
            print('\n' * 5)
            break
        else:
            print('\n\033[1;31mERRO\033[m\nVerifique o valor inserido.\nPor favor, tente novamente.')
            print()
            print('__' * 18)
            input('Pressione \033[1;4mEnter\033[m para voltar ao menu.')
            print('\n' * 5)

print(f'{"Programa encerrado com sucesso":^45}')
print(f'{"Ate logo :D":^45}\n')
