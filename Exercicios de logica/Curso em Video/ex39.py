# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from functions import titulo, erro, pular, press_enter, encerrar, programa_encerrado    # Funcoes que criei.
import datetime  # Sera usado para pegar a data atual.

data_atual = datetime.datetime.now()    # Pegando a data e hora atual.
data = data_atual.date()    # Pegando apenas a data.
ano_atual = data.strftime('%Y')    # Pegando o ano atual.

deseja = 0    # Recebe 1 se o usuario deseja encerrar o programa, recebe 0 se ele nao quiser.

titulo('Alistamento Militar')

while deseja != 1:    # Enquanto o usuario nao desejar encerrar o programa.
    try:
        ano_nascimento = int(input('\nInforme o ano em que voce nasceu: '))    # Pegando o ano em que o usuario nasceu.

    except:
        erro('Por favor\nVerifique os dados informados.')
        pular(5)

    else:
        if ano_nascimento > int(ano_atual):    # Se o ano do nascimento for maior que o ano atual.
            erro('O ano de nascimento nao pode\nser maior que o ano atual.')
            pular(5)

        elif ano_nascimento < 0:    # Se o ano do nascimento for menor que zero.
            erro('O ano de nascimento nao pode\nser menor que zero.')
            pular(5)

        else:
            idade = int(ano_atual) - ano_nascimento    # Idade do usuario.

            if idade < 18:
                tempo_que_falta = 18 - idade    # Os anos que faltam ate o usuario ter 18 anos.

                pular(5)
                print('__' * 21)
                print(f'''Idade: {idade}

É necessario ter 18 anos para se alistar.

Em {int(ano_atual) + tempo_que_falta} voce podera se alistar. 
(Daqui a {tempo_que_falta} anos)''')
                print('__' * 21)
                press_enter('para continuar.')

                deseja = encerrar()    # Perguntando ao usuario se ele deseja encerrar o programa.
                if deseja == 0:    # Se o usuario nao quiser encerrar, o programa ira pular 5 linhas.
                    pular(5)

            elif idade > 18:
                tempo_que_passou = idade - 18    # Os anos que passaram desde que o usuario fez 18 anos.

                pular(5)
                print('__' * 21)
                print(f'''Idade: {idade}

Voce perdeu a epoca de alistamento aos 18.

Em {int(ano_atual) - tempo_que_passou} voce deveria ter se alistado.
({tempo_que_passou} anos atras)''')
                print('__' * 21)
                press_enter('para continuar.')

                deseja = encerrar()
                if deseja == 0:
                    pular(5)

            else:    # Se o usuario fizer 18 anos no ano atual.
                pular(5)
                print('__' * 21)
                print(f'''Idade: {idade}

Voce completa 18 anos esse ano.

Compareça a uma junta de serviço militar
mais proxima da sua casa, ou acesse o 
site: https://alistamento.eb.mil.br/''')
                print('__' * 21)
                press_enter('para continuar.')

                deseja = encerrar()
                if deseja == 0:
                    pular(5)

programa_encerrado()    # Mensagem de despedida quando o programa for encerrado.
