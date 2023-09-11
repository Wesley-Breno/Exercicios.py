"""
Leet spek generator.
Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo.
A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao
mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um
grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e
transforme-o para a grafia leet speak.
"""

texto_informado = str(input('Informe o texto: '))

texto_com_vogais_leet = ''

# Trocando as vogais da frase por numeros
for caractere in texto_informado.lower():
    if caractere == 'a':
        texto_com_vogais_leet += '4'
    elif caractere == 'e':
        texto_com_vogais_leet += '3'
    elif caractere == 'i':
        texto_com_vogais_leet += '1'
    elif caractere == 'o':
        texto_com_vogais_leet += '0'
    elif caractere == 'u':
        texto_com_vogais_leet += 'ü'
    else:
        texto_com_vogais_leet += caractere

print('\nTexto informado:\n'
      f'{texto_informado}\n\n'
      f'Texto em l33t:\n'
      f'{texto_com_vogais_leet}')
