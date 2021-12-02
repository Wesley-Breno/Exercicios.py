# Crie um programa que leia o nome de
# uma cidade diga se ela começa ou não com o nome "SANTO".

from functions import titulo, erro, encerrar, programa_encerrado, pular

deseja = 0  # Variavel para saber se o usuario quer encerrar o programa
while deseja != 1:  # Se "deseja" for igual a 1 o programa encerra
    invalidos = 0   # Contador para ver se o nome tem algum numero ou caractere especial
    titulo('City Names')
    cidade = str(input('Digite o nome de uma cidade...\nNome: ').strip().title())
    for i in cidade:    # Verificando se tem numero ou caractere especial
        if i in '1234567890"!#$%&*()_-+=§{[ª}]º/?°;:.<,>\|¬':
            invalidos += 1
    if invalidos == 0:
        if cidade == '':
            erro('Digite o nome de uma cidade\nPor favor, tente novamente.')
        else:
            cidade_lista = cidade.split()   # Transformando o nome da cidade em uma lista para poder pegar o primeiro nome
            if cidade_lista[0].upper() == 'SANTO' or cidade_lista[0].upper() == 'SANTOS':
                print(f'\n\nA cidade "{cidade}" \033[1;32mcomeça\033[m com santo!')
                deseja = encerrar()
                if deseja == 0:  # Se o usuario nao quiser encerrar o programa ira pular 5 linhas
                    pular(5)
            else:
                print(f'\n\nA cidade "{cidade}" \033[1;31mnão\033[m começa com santo!')
                deseja = encerrar()
                if deseja == 0:
                    pular(5)
    else:
        erro(f'[ {cidade} ]\nNão é possivel usar numeros\ne caracteres especiais.')

programa_encerrado()
