from random import choice
from string import ascii_lowercase, digits, ascii_uppercase


def gerar_senha(qtd_caracteres=16):
    """
    Funcao que gera senhas com caracteres aleatorios com numeros, letras maiusculas e minusculas.
    :param qtd_caracteres: Quantidade de caracteres que a senha tera.
    :return: Retorna a senha com a quantidade de caracteres informada.
    """
    nums = [0, 1, 2]  # Numeros que o programa ira escolher para colocar numero ou letra
    senha = ''

    for c in range(qtd_caracteres):  # Enquanto o programa nao gerar uma senha com o total de caracteres informado
        escolha = choice(nums)
        if escolha == 0:  # Se o programa decidiu colocar um numero
            senha += choice(digits)

        elif escolha == 1:  # Se o programa decidiu colocar uma letra minuscula
            senha += choice(ascii_lowercase)

        else:
            senha += choice(ascii_uppercase)  # Se o programa decidiu colocar uma letra maiuscula

    return senha


if __name__ == '__main__':
    senha1 = gerar_senha()
    senha2 = gerar_senha()
    print(senha1)
    print(senha2)
