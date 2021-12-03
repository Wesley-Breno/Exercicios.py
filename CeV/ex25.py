# Crie um programa que leia o nome
# de uma pessoa e diga se ela tem "SILVA" no nome.

from functions import titulo, erro, pular, encerrar, press_enter, programa_encerrado

deseja = 0
while deseja != 1:
    titulo('Analisador de nome')
    try:
        nome = str(input('Por favor, informe o seu nome...\nNome: ').strip().title())
    except:
        erro('Algo deu errado\nPor favor, tente novamente.')
    else:
        nome_lista = nome.split()
        nome_junto = ''.join(nome_lista)
        if nome_junto.isalpha():
            tem_silva = 0
            for i in nome_lista:
                if i.upper() == 'SILVA':
                    tem_silva += 1
            if tem_silva > 0:
                pular(5)
                print('--' * 17)
                print(f'"{nome}"\n\033[1;32mtem\033[m o sobrenome "silva"!')
                print('--' * 17)
                press_enter()
                deseja = encerrar()
                pular(5)
            else:
                pular(5)
                print('--' * 17)
                print(f'"{nome}"\n\033[1;31mnao\033[m tem o sobrenome "silva"!')
                print('--' * 17)
                press_enter()
                deseja = encerrar()
                pular(5)
        else:
            if nome == '':
                erro(f'Por favor, digite um nome\npara ser analisado.')
                pular(5)
            else:
                erro(f'[ {nome} ]\nO nome nao pode conter nu-\nmeros e caracteres especiais.')
                pular(5)

programa_encerrado()
