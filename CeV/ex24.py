# Crie um programa que leia o nome de
# uma cidade diga se ela começa ou não com o nome "SANTO".

from functions import titulo, erro, encerrar, programa_encerrado, pular

deseja = 0
while deseja != 1:
    invalidos = 0
    titulo('City Names')
    cidade = str(input('Digite o nome de uma cidade...\nNome: ').strip().title())
    for i in cidade:
        if i in '1234567890"!#$%&*()_-+=§{[ª}]º/?°;:.<,>\|¬':
            invalidos += 1
    if invalidos == 0:
        if cidade == '':
            erro('Digite o nome de uma cidade\nPor favor, tente novamente.')
        else:
            cidade_lista = cidade.split()
            if cidade_lista[0].upper() == 'SANTO' or cidade_lista[0].upper() == 'SANTOS':
                print(f'\n\nA cidade "{cidade}" \033[1;32mcomeça\033[m com santo!')
                deseja = encerrar()
                if deseja == 0:
                    pular(5)
            else:
                print(f'\n\nA cidade "{cidade}" \033[1;31mnão\033[m começa com santo!')
                deseja = encerrar()
                if deseja == 0:
                    pular(5)
    else:
        erro(f'[ {cidade} ]\nNão é possivel usar numeros\ne caracteres especiais.')

programa_encerrado()
