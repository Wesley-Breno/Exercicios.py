import re

while True:  # Enquanto o usuario nao digitar o formato correto de um email.
    email = str(input('\nDigite o email: '))

    email_valido = re.findall(r'^(([a-zA-Z\d.]+)@([a-zA-Z]+\.com))$', email)

    if len(email_valido) >= 1:  # Se o usuario digitou o formato correto de um email.

        print('\n\n\t\tDetalhes do email\n')
        print(f'Email completo: {email_valido[0][0]}')
        print(f'Nome do email: {email_valido[0][1]}')
        print(f'Dominio do email: {email_valido[0][2]}')

        break

    else:

        print('\n\n\t\tVoce nao digitou um email valido.\n')
