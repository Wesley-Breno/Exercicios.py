"""
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com
as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o
usuário ganhou ou perdeu o jogo.
"""

from random import shuffle, randint

# Abrindo arquivo onde estao as palavras
with open('palavras.txt', 'r') as file:
    palavras_arquivo = file.readlines()

# Formantando palavras para tirar a quebra de linha e deixar somente cada palavra dentro de uma lista
palavras = []
for palavra in palavras_arquivo:
    palavras.append(str(palavra).replace('\n', '').lower())

palavra_escolhida = palavras[randint(0, len(palavras) - 1)]  # Escolhendo palavra da primeira rodada com base no indice

# Embaralhando palavra
palavra_embaralhada = list(palavra_escolhida)
shuffle(palavra_embaralhada)
palavra_embaralhada = ''.join(palavra_embaralhada)

# Caso a palavra embaralhada acabe sendo igual a palavra normal, ele ira embaralhar ate nao ser mais
while palavra_embaralhada == palavra_escolhida:
    palavra_embaralhada = list(palavra_escolhida)
    shuffle(palavra_embaralhada)
    palavra_embaralhada = ''.join(palavra_embaralhada)

tentativas = 6

# Enquanto o nao perder 6 vezes seguidas
while tentativas != 0:
    palpite_palavra = str(input(f'Qual palavra é "{palavra_embaralhada}"?\nA palavra é: ')).strip().lower()

    # Se acertou a palavra
    if palpite_palavra == palavra_escolhida:
        print('\n\n\t\tParabens! Voce \033[;32macertou\033[m!!\n\n')

        tentativas = 6  # Colocando numero de tentativas no valor padrao

        # Escolhendo nova palavra e embaralhando ela
        palavra_escolhida = palavras[randint(0, len(palavras) - 1)]
        palavra_embaralhada = list(palavra_escolhida)
        shuffle(palavra_embaralhada)
        palavra_embaralhada = ''.join(palavra_embaralhada)

        # Caso a palavra embaralhada acabe sendo igual a palavra normal, ele ira embaralhar ate nao ser mais
        while palavra_embaralhada == palavra_escolhida:
            palavra_embaralhada = list(palavra_escolhida)
            shuffle(palavra_embaralhada)
            palavra_embaralhada = ''.join(palavra_embaralhada)

    else:
        tentativas -= 1
        print(f'\n\n\t\tOH NAO! Voce \033[;31merrou\033[m!! \n\t\tFaltam {tentativas} tentativas\n\n')

print('\n\n\t\t[ \033[;31mGAME OVER\033[m ]')
print(f'\
t  A palavra era: {palavra_escolhida}\n\n')
