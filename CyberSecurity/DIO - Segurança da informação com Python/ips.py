from ipaddress import ip_address

ip_endereco = str(input('Informe o endereco IP: '))

try:  # Usando funcao do ipaddress para saber se o ip é valido
    ip = ip_address(ip_endereco)

except ValueError:  # Se o ip for invalido
    print(f'\nO ip "{ip_endereco}" \033[;31mnão\033[m é um ip valido.')

else:  # Se o ip for valido
    print(f'\nO ip "{ip_endereco}" é um ip \033[;32mvalido\033[m.')
