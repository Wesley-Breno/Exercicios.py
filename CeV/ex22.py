# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

from functions import titulo, erro, pular, encerrar     # Importando as funções que serao usadas

deseja = 0  # Variavel para saber se o usuario deseja encerrar
while deseja != 1:
    total_de_letras = 0  # Total de letras do nome completo
    erros = 0  # Se houve algum erro com a interaçao com o usuario
    titulo('Nome do usuario')
    try:
        nome = str(input('\nDigite o seu nome completo: ').title().strip())
    except:
        erro('Digite um nome que seja valido.')
        erros += 1
    else:
        if len(nome) <= 2:
            erro('O nome nao pode conter menos\nque 3 caracteres.')
            erros += 1
        if nome in "!@#$%*()_+{}?><|'\.,/°º][^~´-¬¢£§=" or nome.isnumeric():    # Saber se tem algum caractere especial ou numero
            erro('O nome nao pode conter\nnumeros/caracteres especiais.')
            erros += 1
        for l in nome:  # Saber se tem algum numero no nome
            if l.isnumeric():
                erro('O nome nao pode conter\nnumeros/caracteres especiais.')
                erros += 1
        for l in nome:  # Contar quantas letras tem mas sem contar com os espaços ' '
            if l != '' and l != ' ':
                total_de_letras += 1
        primeiro_nome = nome.split()    # Cada nome vira uma lista
        total_de_letras_do_primeiro_nome = len(primeiro_nome[0])    # Pegando o total de letras do primeiro nome
        if erros != 0:  # Se tiver algum erro na interaçao com o usuario, o programa ira começar tudo de novo.
            pass
        else:   # Se nao tiver nenhum erro, o programa ira mostrar as informaçoes do nome.
            pular(2)
            print('__' * 26)
            print(f'''Seu nome: \t\t\t{nome}
Nome em maiusculo: \t{nome.upper()}
Nome em minusculo: \t{nome.lower()}
Total de letras: \t{total_de_letras}
Primeiro nome: \t\t{primeiro_nome[0]}
Total de letras: \t{total_de_letras_do_primeiro_nome}''')
            print('__' * 26)
            deseja = encerrar()

pular(3)
print(f'{"Programa finalizado com sucesso":^45}')
print(f'{"Ate logo :)":^45}')
pular(3)
