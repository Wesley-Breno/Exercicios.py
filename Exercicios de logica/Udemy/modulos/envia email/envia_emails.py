import smtplib  # Modulo responsavel por fazer login e enviar email
from email.message import EmailMessage  # Responsavel por informar o titulo, mensagem e quem ira receber o email

print('\n\n\t\t\033[;1mLogin\033[m\n\n')
# Pegando email e senha do remetente
email_remetente = str(input('Informe o seu email: '))
senha_remetente = str(input('Informe a senha: '))

print('\n\n\t\t\033[;1mQuem vai receber o email\033[m\n\n')
email_destinatario = str(input('Informe o email do destinatário: '))  # Pegando email de quem recebera os emails

print('\n\n\t\t\033[;1mInformacoes do email\033[m\n\n')

msg = EmailMessage()
msg['From'] = email_remetente  # Informando quem enviou o email
msg['To'] = email_destinatario  # Informando para quem vai o email
msg['Subject'] = str(input('Digite o titulo do email: '))  # Escrevendo o titulo do email
msg.set_content(str(input('Digite a mensagem: ')))  # Escrevendo a mensagem do email

print('\n\n\t\tRepeticoes\n\n')
encerrar = False  # Variavel para saber se é a hora de encerrar o programa
houve_erro = 0  # Variavel para saber se houve algum erro ao tentar enviar o email

while not encerrar:  # Enquanto o usuario nao digitar um numero inteiro corretamente
    try:
        cont = int(input('Quantas vezes deseja enviar esse email: '))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Adicione um numero inteiro novamente.\n\n')

    else:
        print('Enviando email... \033[;37maguarde\033[m')

        while cont != 0:  # Enquanto o programa nao enviar a quantidade de emails informada
            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Entrando no site
                    smtp.login(email_remetente, senha_remetente)  # Logando na conta
                    smtp.send_message(msg)  # Enviando email

            except:
                print('\n\n\t\t[\033[;31mERRO\033[m]: erro ao tentar enviar email'
                      '\n\t- Verifique email do destinatario'
                      '\n\t- Verifique seu email e senha'
                      '\n\t- Tente novamente\n\n')
                houve_erro = 1
                encerrar = True  # O programa sera encerrado
                cont = 0  # Recebe 0 pra parar de tentar enviar email ja que houve um erro

            else:
                encerrar = True  # O programa sera encerrado quando enviar todos os emails
                cont -= 1

        if houve_erro != 1:  # Se nao houve nenhum erro enquanto o programa tentava enviar os emails
            print('\n\n\t\tEmail enviado com \033[;32msucesso\033[m :)\n\n')
