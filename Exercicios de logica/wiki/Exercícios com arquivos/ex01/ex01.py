"""
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e
gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

O arquivo de entrada possui o seguinte formato:
    200.135.80.9
    192.168.1.1
    8.35.67.74
    257.32.4.5
    85.345.1.2
    1.2.3.4
    9.8.234.5
    192.168.0.256

O arquivo de saída possui o seguinte formato:
    [Endereços válidos:]
    200.135.80.9
    192.168.1.1
    8.35.67.74
    1.2.3.4

    [Endereços inválidos:]
    257.32.4.5
    85.345.1.2
    9.8.234.5
    192.168.0.256
"""

from ipaddress import ip_address

ips_validos = []
ips_invalidos = []

# Abrindo arquivo txt com os ips e colocando em uma lista
with open('ips.txt', 'r') as file:
    ips = [ip.replace('\n', '') for ip in file.readlines()]  # Removendo a quebra de linha e deixando so o ip

# Iterando sobre os ips e vendo qual é valido e qual nao é
for ip in ips:
    try:
        ip_address(ip)
        ips_validos.append(ip)
    except ValueError:  # Se der erro, o ip é invalido
        ips_invalidos.append(ip)

print('[Enderecos validos:]')
for ip in ips_validos:  # Mostrando cada ip valido
    print(ip)

print('\n[Enderecos invalidos:]')
for ip in ips_invalidos:
    print(ip)
