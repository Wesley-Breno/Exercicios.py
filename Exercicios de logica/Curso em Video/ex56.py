"""
Desenvolva um programa que leia o nome,
idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

from functions import titulo, press_enter, pular, programa_encerrado, linha, erro, encerrar    # Funções que criei.


titulo('Informações')
press_enter()

while True:    # Enquanto o usuario nao preencher as informações e nao quiser encerrar.

    pessoas = {}
    grupo, idades, idades_masculinas, masculino_mais_velho = [], [], [], []
    soma_da_idade, media_da_idade, maior_idade_masculina, cont, mulhers_menos_de_20, deseja_encerrar = 0, 0, 0, 0, 0, 0
    erros = 0    # Contador de erros na adição de informações, se for maior que zero, o programa se reinicia.

    pular(5)
    for c in range(0, 4):
        print(f'{c + 1}º USUARIO')
        linha('__', 24)
        try:
            pessoas['nome'] = str(input('Digite o nome de usuario: ')).capitalize().strip().split()
            pessoas['idade'] = int(input('Digite a idade: '))
            pessoas['sexo'] = str(input('Digite o sexo [ M - Masculino ] - [ F - Feminino ]: ')).upper().strip()[0]
        except:
            erro('Por favor\nInsira as informações corretamente.')
            erros += 1
            break
        else:
            linha('__', 24)
            grupo.append(pessoas.copy())
            pessoas.clear()

    for p in grupo:    # Verificando se o usuario digitou as informações das idades erradas.
        if p['sexo'] not in 'FM':
            erro('Por favor\nDigite o sexo corretamente.')
            erros += 1
            break

    if erros > 0:    # Se tiver algum erro o programa se reinicia.
        continue

    for p in grupo:
        if p['sexo'] == 'M':    # Pegando as idades masculinas para poder compara-las.
            idades_masculinas.append(p['idade'])
        else:
            if p['idade'] <= 20:    # Pegando as idades das mulheres que tem menos de 20.
                mulhers_menos_de_20 += 1

        idades.append(p['idade'])
        soma_da_idade += p['idade']

    media_da_idade = soma_da_idade / (len(idades))

    for i in idades_masculinas:    # Comparando as idades masculinas, para ver qual é a maior idade.
        if cont == 0:    # Contador para saber se é a primeira vez que se esta comparando.
            maior_idade_masculina = i
            cont += 1
        else:
            if maior_idade_masculina < i:
                maior_idade_masculina = i

    for p in grupo:    # Pegando o primeiro nome do homem mais velho.
        if p['sexo'] == 'M':
            if p['idade'] == maior_idade_masculina:
                masculino_mais_velho.append(p['nome'][0])

    pular(5)
    linha('__', 24)
    print(f'|> Media de idade do grupo: {int(media_da_idade)}')
    if len(masculino_mais_velho) <= 0:
        print('|> Nome do homem mais velho do grupo: \033[;37m(Não foi encontrado nenhum homem)\033[m')
    else:
        if len(masculino_mais_velho) > 1:
            print(f'|> Nomes dos homens mais velhos do grupo: {masculino_mais_velho}')
        else:
            print(f'|> Nome do homem mais velho do grupo: {masculino_mais_velho}')
    if mulhers_menos_de_20 <= 0:
        print("|> Quantas mulheres tem menos de 20 anos: "
              "\033[;37m(Não foi encontrada nenhuma mulher com menos de 20 anos)\033[m")
    else:
        print(f'|> Quantas mulheres tem menos de 20 anos: {mulhers_menos_de_20}')
    linha('__', 24)
    press_enter()

    deseja_encerrar = encerrar()
    if deseja_encerrar == 1:
        break

programa_encerrado()
