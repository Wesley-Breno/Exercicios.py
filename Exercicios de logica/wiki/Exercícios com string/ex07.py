"""
Conta espaços e vogais.
Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
* quantos espaços em branco existem na frase.
* quantas vezes aparecem as vogais a, e, i, o, u.
"""

total_espacos_em_branco = 0
total_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

frase = str(input('Informe a frase: '))

# Fazendo soma de quantos espacos em brancos tem e quantas vogais
for caractere in frase.lower():
    if caractere == ' ':  # Se o caractere for um espaco em branco
        total_espacos_em_branco += 1

    for chave in total_vogais.keys():  # Para cada chave de vogais no dicionario
        if caractere == chave:  # Se o caractere for uma vogal
            total_vogais[caractere] += 1

print(f"""
Frase: {frase}

Total de espacos em branco: {total_espacos_em_branco}
[ Total de vogais ]""")
for vogal, quantidade in total_vogais.items():  # Mostrando cada vogal e a quantidade de vezes que ela aparece
    print(f'\t{vogal.upper()} = {quantidade}')
