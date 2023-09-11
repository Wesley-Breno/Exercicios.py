"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

aluno = dict()  # Dicionario que vai conter o nome, media e situacao do aluno.

while True:  # Enquanto o programa nao pegar os dados do aluno
    nome = str(input('Informe o nome do aluno: '))

    if len(nome) >= 3 and nome.isalpha():  # Se o nome tiver mais de 3 caracteres e so conter letras

        try:
            media = float(input('Informe a media do aluno: '))

        except ValueError:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Informe a media do aluno.\n\n')

        else:
            if 0 <= media <= 10:  # Se a media informada estiver entre o numero 0 e 10
                aluno['nome'] = nome
                aluno['media'] = media

                if media >= 7:
                    aluno['situacao'] = 'Aprovado'
                elif 7 > media >= 5:
                    aluno['situacao'] = 'Recuperacao'
                else:
                    aluno['situacao'] = 'Reprovado'

                break  # Quebrando repeticao para mostrar os dados

            print('\n\n\t\t[\033[;31mERRO\033[m]: Informe a media correta.\n\n')

    else:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Digite seu nome completo\n\n')

# Printando o resultado dos dados informados
print('--' * 20)
print(f'''\t\tDados do aluno

\tNome do aluno: {aluno["nome"]}
\tMedia do aluno: {aluno["media"]}
\tSituacao do aluno: {aluno["situacao"]}
\n\n''')
