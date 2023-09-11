"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá
uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""

from random import choice  # Funcao que sera usada para escolher uma palavra aleatoria

# Abrindo arquivo onde estao as palavras
with open('palavras.txt', 'r') as file:
    palavras = file.readlines()

# Formantando palavras para tirar a quebra de linha e deixar somente a palavra
palavras_formatadas = []
for palavra in palavras:
    palavras_formatadas.append(str(palavra).replace('\n', ''))

# Definindo palavra aleatoria escolhida, tentativas e a lista que ira conter as palavras informadas da primeira rodada
palavra_escolhida = choice(palavras_formatadas)
tentativas = 6
letras_informadas = []

# Enquanto o usuario nao perder todas as 6 tentativas
while tentativas != 0:
    print()

    # Mostrando na tela as palavras restantes
    print('A palavra é -> ', end='')
    for caractere in palavra_escolhida.lower():
        if caractere in letras_informadas:  # Se a letra informada estiver na palavra escolhida
            print(caractere, end='')
        else:
            print('_', end='')

    # Comparando caracteres informados com a palavra escolhida e contando +1
    cont = 0
    for caractere in palavra_escolhida.lower():
        if caractere in letras_informadas:
            cont += 1

    # Se o usuario acertou a palavra
    if cont == len(palavra_escolhida):
        print('\n\n\t\t\033[;32mVoce acertou!!!\033[m\n')
        tentativas = 6  # Reiniciando tentativas
        palavra_escolhida = choice(palavras_formatadas)  # Escolhendo nova palavra
        letras_informadas = []  # Esvaziando lista de letras informadas

        print(f'A palavra é -> {"_" * len(palavra_escolhida)}')  # Mostrando quantidade de caracteres da nova palavra

    # Recebendo uma letra informada pelo usuario
    try:
        letra_rebecida = str(input('\nInforme a letra: ')).lower()[0]
    except IndexError:
        letra_rebecida = str(input('\nInforme a letra: ')).lower()[0]

    # Se o usuario acertou a letra que informou
    if letra_rebecida in palavra_escolhida.lower() and letra_rebecida not in letras_informadas:
        letras_informadas.append(letra_rebecida)

    else:
        # Se o usuario ja informou a letra
        if letra_rebecida in letras_informadas:
            print('\n\t\t\033[;37m[Voce ja informou essa letra]\033[m')

        else:
            tentativas -= 1

            if tentativas != 0:  # Se o usuario ainda tem tentativas
                letras_informadas.append(letra_rebecida)
                print(f'\n\n\t\t\033[;31mVoce errou! ({tentativas} tentativas restantes)\033[m\n')

print('\n\n\t\t\033[;31m_-Game Over-_\033[m\n'
      f'\tA palavra era: {palavra_escolhida}')
