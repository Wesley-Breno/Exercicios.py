"""
Este software faz a verificacao de IP ou HOST que foi informado pelo usuario com uso da funcao.
"""

import os  # Importando modulo OS para fazer um comando no sistema


def verification(ip_host: str, times=1) -> None:
    if times == 1:  # Se o usuario noa informou a qunatidade de vezes que deseja fazer a verificacao
        os.system(f'ping {ip_host}')
    else:
        os.system(f'ping -n {times}, {ip_host}')


if __name__ == "__main__":
    verification('www.google.com', 10)  # Fazendo verificacao do google
