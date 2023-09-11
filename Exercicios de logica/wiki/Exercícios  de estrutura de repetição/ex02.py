"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
mensagem de erro e voltando a pedir as informações.
"""

while True:  # Enquanto o usuario nao informar o nome e senha validos
    try:
        nome_usuario = str(input('\nDigite o nome de usuario\nNome: '))
        senha = str(input('\nDigite a senha\nSenha: '))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe o nome de usuario e senha novamente.')

    else:
        if nome_usuario == senha:  # Se o nome de usuario for igual a senha
            print('\n\n\t\t[\033[;31mERRO\033[m]: Voce nao pode usar o nome de usuario como senha.')

        else:
            print('\n\n\t\tNome de usuario e senha validados ✔')
            break
