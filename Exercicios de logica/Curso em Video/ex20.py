# O professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# Importei todas as funcoes que usei no programa
from random import randint
from functions import titulo, erro, pular, encerrar


deseja = 0  # Se esta variavel receber o valor 1 significa que o usuario deseja encerrar o programa.
while deseja != 1:  # Repeticao para o programa continuar rodando

    alunos = []     # Lista dos nomes dos alunos
    tem_nome_errado = 0     # Variavel vai receber 1 se tiver algum nome com numero ou caractere especial
    titulo('Ordem de apresentação')
    try:    # Fazendo o tratamento de erros
        quantidade_de_alunos = int(input('Digite a quantidade de alunos que irao\nparticipar do sorteio da ordem.\n\nTotal de alunos: '))
    except:
        erro('Verifique os dados inseridos.')
    else:
        if quantidade_de_alunos <= 0 or quantidade_de_alunos == 1:  # Se a quantidade de alunos for menor ou igual a zero ou a quantidade de alunos for igual a 1
            if quantidade_de_alunos == 1:
                erro('Nao é possivel fazer o \nsorteio com \033[4;1m1\033[m pessoa só.')
            else:
                erro('Nao é possivel fazer o \nsorteio com \033[4;1m0\033[m pessoas.')
        else:
            pular(3)
            print(f'\033[1;4m ADICIONE OS {quantidade_de_alunos} ALUNOS \033[m')
            for c in range(0, quantidade_de_alunos):    # Adicionando os alunos
                alunos.append(str(input(f'Digite o nome do {c + 1}° aluno: ').strip().capitalize()))
            for a in alunos:    # Verificando se tem algum erro no nome
                for l in a:
                    if l.isnumeric() or l in '!@#$%"&*()_+=-.,/\|:;><^~`[]{}':
                        tem_nome_errado += 1
                        nome_errado = a
                        erro(f'Nao aceitamos caracteres\nespecias e numeros nos nomes.\n\n[ {nome_errado} ]')
            if tem_nome_errado == 0:    # Se nao tiver nenhum nome errado
                print('\n\n\033[1;4m ORDEM DE APRESENTAÇÃO \033[m')
                sorteio = []
                while len(sorteio) != len(alunos):  # Enquanto a lista sorteio nao tiver a mesma quantidade que a lista alunos
                    for c in range(len(alunos)):
                        numero_aleatorio = randint(0, len(alunos) - 1)
                        if numero_aleatorio not in sorteio:     # Se o numero aleatorio que sera usado para sortear, nao estiver na lista, ele ira ser adicionado
                            sorteio.append(numero_aleatorio)
                cont = 0
                for i in sorteio:   # Mostrando os alunos sorteados
                    cont += 1
                    print(f'{cont}° > {alunos[i]}')
                deseja = encerrar('sorteio')    # Funcao perguntando se o usuario deseja encerrar

pular(5)
print(f'{"Programa finalizado com sucesso":^45}')
print(f'{"Ate logo :)":^45}')
pular(5)
