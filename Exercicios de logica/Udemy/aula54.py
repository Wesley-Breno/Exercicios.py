from functions import titulo, press_enter, pular, erro, encerrar, programa_encerrado

titulo('Aula 54')
press_enter('para iniciar.')

deseja = 0
while deseja != 1:
    pular(25)
    print(f'\033[;1m{"Menu de escolha":^45}\033[m')     # Menu onde aparecera as escolhas disponiveis
    print('''\nDigite o numero da escolha que deseja fazer...
    
\033[1;31m1\033[m ➤ Exercício 1.
\033[1;31m2\033[m ➤ Exercício 2.
\033[1;31m3\033[m ➤ Exercício 3.
\033[1;31m4\033[m ➤ Exercício 4.
\033[1;31m5\033[m ➤ Informações.
\033[1;31m0\033[m ➤ \033[1;31mSair.\033[m''')
    print('──' * 15)

    try:
        escolha = int(input('Escolha: '))
    except:
        pular(25)
        erro('Digite apenas uma das\nescolhas que foram mostradas.')
        pular(25)
    else:
        if escolha == 1:    # Exercicio 1
            pular(25)
            print(f'\033[;1m{"Saudação":^45}\033[m\n\n')

            def ola(saudacao='Ola', nome='Usuario.'):
                """
                Função que ira escrever uma mensagem de saudação para
                o usuario.
                :param saudacao: parametro que ira ser a mensagem de saudação
                :param nome: parametro que ira ser o nome do usuario
                :return: None
                """
                print(saudacao, nome)

            ola()
            pular()
            press_enter('para voltar ao menu.')

        elif escolha == 2:  # Exercicio 2
            pular(25)
            print(f'\033[;1m{"Soma":^45}\033[m\n\n')

            def soma(n1=0, n2=0, n3=0):
                """
                Função que tera 3 valores como parametro e depois somar
                eles e mostrar na tela.
                :param n1: primeiro numero.
                :param n2: segundo numero.
                :param n3: terceiro numero.
                :return: None
                """
                print(f'A soma entre {n1}, {n2}, {n3}.\nEquivale a: \033[;1m{n1 + n2 + n3}\033[m')

            soma(1, 2, 4)
            pular()
            press_enter('para voltar ao menu.')

        elif escolha == 3:  # Exercicio 3
            pular(25)
            print(f'\033[;1m{"Aumento percentual":^45}\033[m\n\n')

            def aumento_percentual(numero, aumento):
                """
                Função de 2 parametros que ira pegar um valor e
                depois fazer um aumento de acordo com o valor do
                segundo parametro.
                :param numero: valor que ira ser feito o aumento.
                :param aumento: a porcentagem que ira ser adicionada no valor.
                :return: Retorna o valor com o acrescimo da porcentagem
                """
                return numero + (numero * aumento / 100)

            aumento = aumento_percentual(50, 20)  # Pegar o valor 50 e adicionar mais 20% de valor
            print(f'Aumento percentual com base nos parametros.\n─>', int(aumento))
            pular()
            press_enter('para voltar ao menu.')

        elif escolha == 4:  # Exercicio 4
            pular(25)
            print(f'\033[;1m{"Fizz-Buzz":^45}\033[m\n\n')

            def fizz_buzz(n):
                """
                Função que ira calcular o valor colocado no parametro
                e conforme a condição ele ira mostrar uma mensegem...

                FizzBuzz
                    Para se o valor for divisivel por 3 e 5
                Fizz
                    Para se o valor for divisivel apenas por 3
                Buzz
                    Para se o valor for divisivel apenas por 5
                :param n: Parametro que ira ser colocado o valor que ira ser calculado
                :return: Retorna a mensagem ou o propio valor caso ele não seja divisivel por nenhuma das alternativas
                """
                if n % 3 == 0 and n % 5 == 0:
                    return 'FizzBuzz'
                elif n % 3 == 0:
                    return 'Fizz'
                elif n % 5 == 0:
                    return 'Buzz'
                else:
                    return n

            resultado = fizz_buzz(15)
            print(resultado)
            pular()
            press_enter('para voltar ao menu.')

        elif escolha == 5:  # Informações do programa
            pular(25)
            print(f'\033[1;37m{"Informações":^45}\033[m\n')
            print('''\033[;37m
    Aqui estão os 4 exercícios feitos na aula 54
    do curso do Otavio Miranda, na plataforma Udemy.
    
    Abaixo esta cada exercício e oque foi pedido.

    \033[1;4;37mExercício 1\033[m\033[;37m;
        Crie uma função que exibe uma saudação com
        os parâmetros 'saudacao' e 'nome'.
    
    \033[1;4;37mExercício 2\033[m\033[;37m;
        Crie uma função que receba 3 números como
        parâmetros e exiba a soma entre eles.
        
    \033[1;4;37mExercício 3\033[m\033[;37m;
        Crie uma função que receba 2 números. O
        primeiro é um valor e o segundo um per-
        centual (ex. 10%). Retorne (return) o
        valor do primeiro número somado do au-
        mento do percentual do mesmo.
        
    \033[1;4;37mExercício 4\033[m\033[;37m;
        Fizz - Buzz
        Se o parâmetro da função for divisível
        por 3, retorne fizz, se o parâmetro da 
        função for divisível por 5, retorne
        buzz. Se o parâmetro da função for di-
        visível por 5 e por 3, retorne FizzBuzz,
        caso contrário, retorne o número enviado.
        \033[m''')
            press_enter()

        elif escolha == 0:  # Se o usuario quiser encerrar o programa
            pular(25)
            deseja = encerrar()

        else:
            pular(25)
            erro('Digite apenas uma das\nescolhas que foram mostradas.')
            pular(25)

pular(25)
programa_encerrado()
