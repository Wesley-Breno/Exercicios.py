import itertools  # Biblioteca que sera usada para fazer permutações

caracteres = str(input('\nInforme os caracteres que deseja fazer permutações de senha\nCaracteres: '))

senhas = itertools.permutations(caracteres, len(caracteres))  # Fazendo permutações

print('\n\n\t\t[ Permutações de senhas ]\n')
for senha in senhas:  # Mostrando cada permutação
    print(''.join(senha))
