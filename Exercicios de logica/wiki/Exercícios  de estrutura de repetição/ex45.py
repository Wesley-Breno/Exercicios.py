"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota
(atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai
utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos
alunos usarem o programa.
"""

from time import sleep  # Fazendo o programa demorar para executar seu proximo trecho de codigo

alunos = dict()
aluno_id = 1
continuar = True  # Variavel que ira receber False caso nao haja mais alunos para fazer a prova
maior_acerto = None  # Variavel que ira conter o aluno com maior pontos
menor_acerto = None  # Variavel que ira conter o aluno com menor pontos

questoes = dict()
cont = 1  # Contador para saber a quantidade de questoes que ja foram adicionadas
letras = ['A', 'B', 'C', 'D', 'E']

while True:  # Enquanto o professor nao informar os dados das questoes
    if cont == 11:
        break

    letras_e_valores = dict()
    nome_da_questao = str(input(f'\nInforme qual é a {cont}º questão: '))

    for letra in letras:
        letras_e_valores[letra] = str(input(f'Informe o valor que tera na letra {letra}: '))

    resposta_correta = str(input('Informe a letra que esta com a resposta correta: ')).upper()

    if resposta_correta in letras:  # A letra que contem a resposta correta estiver na lista de letras que a prova tem
        questoes[cont] = {'nome_questao': nome_da_questao, 'letras_e_valores': letras_e_valores, 'resposta': resposta_correta}  # Adicionando questao ao dicionario
        cont += 1
    else:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Coloque as informações da prova corretamente.\n\n')
        sleep(2)

while True:  # Enquanto tiver alunos para responderem a prova
    if not continuar:  # Se nao tiver mais alunos para responderem a prova
        break

    respostas = []  # Variavel que ira conter a resposta de cada questao dos alunos

    for chave, valor in questoes.items():  # Fazendo o aluno responder as questoes da prova
        print()
        print('---' * 12)
        print(f'{chave}º Questão')

        for chave, valor in valor.items():
            if chave == 'letras_e_valores':  # Mostrando na tela cada letra e cada valor que elas tem
                for letra, valor in valor.items():
                    print(f'\t[ {letra} ] -> {valor}')

            elif chave == 'resposta':  # Ignorando a resposta para nao ser mostrada ao aluno
                ...

            else:
                print(f'\t{valor}')  # Mostrando pergunta da questao

        resposta = str(input('A resposta esta na letra: ')).upper()  # Perguntando em qual letra esta a resposta correta
        if resposta in letras:  # Se a resposta informada for uma das letras da prova
            respostas.append(resposta)
        else:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Digite a letra que corresponde a resposta que deseja.\n\n')
            sleep(2)

    if len(respostas) > 0:  # Se o usuario respondeu todas as questoes
        cont = 0  # Contador para pegar cada resposta do aluno
        pontos = 0  # Pontos do aluno

        for chave, valor in questoes.items():  # Verificando se a resposta do aluno for igual a resposta certa
            for chave, valor in valor.items():
                if chave == 'resposta':
                    if valor == respostas[cont]:
                        pontos += 1
                    cont += 1

        alunos[aluno_id] = {'respostas': respostas, 'pontos': pontos}
        aluno_id += 1

        while True:  # Enquanto o usuario nao informar se tem mais alguem para fazer a prova
            try:
                continuar = int(input('\n\nHa mais algum aluno para fazer a prova?\n'
                                      '[ 1 ] - Sim\n'
                                      '[ 2 ] - Não\n'
                                      'Resposta: '))
            except ValueError:
                print('\n\n\t\t[\033[;31mERRO\033[m]: Digite o numero que corresponde a resposta que deseja.\n\n')
                sleep(2)

            else:
                if continuar == 1:  # Se o usuario informo que ainda tem alunos para fazerem a prova
                    break

                elif continuar == 2:  # Se não tiver mais alunos para fazerem a prova
                    continuar = False
                    break

                else:
                    print('\n\n\t\t[\033[;31mERRO\033[m]: Digite o numero que corresponde a resposta que deseja.\n\n')
                    sleep(2)

print('\n\n\t\tResultado da turma')

todos_os_pontos = []

for aluno, dados in alunos.items():  # Pegando os pontos de cada aluno
    for chave, valor in dados.items():
        if chave == 'pontos':
            todos_os_pontos.append(valor)

for aluno, dados in alunos.items():  # Verificando qual aluno tem a maior e menor contagem de pontos
    for chave, valor in dados.items():
        if chave == 'pontos':
            if valor == max(todos_os_pontos):
                maior_acerto = f'{aluno}º aluno', valor
            elif valor == min(todos_os_pontos):
                menor_acerto = f'{aluno}º aluno', valor

total_alunos = len(alunos)
media_dos_pontos = sum(todos_os_pontos) / len(todos_os_pontos)  # Media dos pontos de todos os alunos

print(f"""Aluno com maior acerto: {maior_acerto[0]} = {maior_acerto[1]} pontos
Aluno com menor acerto: {menor_acerto[0]} = {menor_acerto[1]} pontos
Media dos pontos da turma: {media_dos_pontos:.1f}
Total de alunos: {total_alunos}

\t\t[ Gabarito ]\n""")

for questao, dados in questoes.items():  # Mostrando qual era a resposta certa de cada questao
    print(f'{questao}º Questão')
    for chave, valor in dados.items():
        if chave == 'resposta':
            print(f'\tResposta: {valor}')
