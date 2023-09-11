"""
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia
uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
"""

import unicodedata  # Modulo que sera usado para tirar os acentos da frase
import string  # Modulo que sera usado para tirar as pontuacoes

frase = str(input('Digite a frase: '))

# Formatando frase
frase_formatada_ordem_certa = ''.join(frase.strip().upper().split())  # Tirando espacos e colocando em maiusculo para comparar
frase_formatada_ordem_certa = ''.join(ch for ch in unicodedata.normalize('NFKD', frase_formatada_ordem_certa) if not unicodedata.combining(ch))  # Retirando acentos
frase_formatada_ordem_certa = frase_formatada_ordem_certa.translate(str.maketrans("", "", string.punctuation))  # Retirando pontuacoes

frase_formatada_ao_contrario = ''

for c in range(len(frase_formatada_ordem_certa) - 1, -1, -1):  # Colocando a frase ao contrario em uma variavel
    frase_formatada_ao_contrario += frase_formatada_ordem_certa[c]

print()
# Comparando frase na ordem certa e ao contrario
if frase_formatada_ordem_certa == frase_formatada_ao_contrario:
    print(f'A frase:\n'
          f'"{frase}"\n'
          f'É palíndromo!')
else:
    print(f'A frase:\n'
          f'"{frase}"\n'
          f'Não é palíndromo!')
