import phonenumbers  # Biblioteca que sera usada para analisar numero de telefone recebido pelo usuario
from phonenumbers import geocoder, carrier  # Funções para pegar a cidade, estado e operadora do numero informado

print('\n\n\t\t\033[;37mDigite [ 0 ] para encerrar o programa\033[m\n')
while True:  # Enquanto o usuario nao digitar 0
    numero = input('\nInforme o numero de telefone com o formato +551140028922\nNumero de telefone: ').replace('-', '').replace(' ', '').replace('(', '').replace(')', '')

    if numero == '0':  # Se o usuario digitou 0
        break

    try:
        telefone_numero = phonenumbers.parse(numero)  # Criando o objeto numero
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe o numero da forma deste exemplo: +551140028922\n\n')
    else:
        # Se o numero for valido com base no algoritmo da biblioteca phonenumbers
        if phonenumbers.is_valid_number(telefone_numero) and phonenumbers.is_possible_number(telefone_numero):
            estado = geocoder.description_for_number(telefone_numero, 'pt')
            pais = geocoder.country_name_for_number(telefone_numero, 'pt')
            formato_nacional = phonenumbers.format_number(telefone_numero, phonenumbers.PhoneNumberFormat.NATIONAL)
            formato_internacional = phonenumbers.format_number(telefone_numero, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            operadora = carrier.name_for_number(telefone_numero, 'pt')
            tipo = phonenumbers.number_type(telefone_numero)

            print()
            print('---' * 20)
            print(f"""        Informações basicas do numero
    
    País/Estado \033[;31m→\033[m {pais} - {estado}
    Operadora \033[;31m→\033[m {'Desconhecida' if operadora == '' else operadora}
    Tipo de dispositivo \033[;31m→\033[m {'Telefone fixo' if tipo == 0 else 'Telefone celular'} 
    Formato internacional \033[;31m→\033[m {formato_internacional}
    Formato nacional \033[;31m→\033[m {formato_nacional}""")
            input('\n\n\t\tPressione ENTER para continuar\n\n')
        else:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Numero nao encontrado... Verifique os caracteres.\n\n')
            input('\n\n\t\tPressione ENTER para continuar\n\n')
