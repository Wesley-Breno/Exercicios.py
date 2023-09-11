from itertools import combinations, permutations, product


def gerator(*args):
    yield args


# Nomes que serao usados de exemplo.
nomes_exemplo = list(gerator('werli', 'fernando', 'jessica', 'guilherme', 'cristian', 'gustavo'))

# Dicionario em um gerador onde tem a explicacao de cada funcao.
explicacoes = gerator({'combinations': 'A função combination() nao tem ordem como prioridade, portanto,\nela ira '
                                       'escrever as '
                                       'combinações considerando tambem ao contrario.\nExemplo;\n\n("werli", '
                                       '"fernando") == '
                                       '("fernando", "werli")',

                       'permutations': 'Ja a função permutation tem a ordem como preferencia\nentao ela ira escrever '
                                       'todas as '
                                       'possibilidades considerando a ordem\nExemplo;\n\n("werli", "fernando")\n'
                                       '("fernando", "werli")',

                       'product': 'E a funçao product mostra todas as combinaçoes possiveis\nate repetindo valores que '
                                  'sao '
                                  'iguais. \nExemplo;\n\n("werli", "werli")\n("werli", "fernando")\n("fernando", '
                                  '"fernando") '
                                  '\n("fernando", "werli")'})

# Usando as funcoes para mostrar como elas trabalham.
combinations_exemplo = (f'\t{*nome,}' for tupla in nomes_exemplo for nome in combinations(tupla, 2))
permutations_exemplo = (f'\t{*nome,}' for tupla in nomes_exemplo for nome in permutations(tupla, 2))
product_exemplo = (f'\t{*nome,}' for tupla in nomes_exemplo for nome in product(tupla, repeat=2))

cont = 0  # Contador para saber quando deve mostrar a explicacao de cada funcao.

for tupla in explicacoes:  # Desempacotando o iterador.
    for dicionario in tupla:  # 'Entrando' no dicionario.
        for chave, valor in dicionario.items():

            if cont == 0:  # Se for para mostrar a primeira explicacao.
                for v in combinations_exemplo:
                    print(v)

            elif cont == 1:
                for v in permutations_exemplo:
                    print(v)

            else:
                for v in product_exemplo:
                    print(v)

            print(f'\n\n\t\033[;1m{chave}\033[m\n\n{valor}\n')
            print('--' * 45)
            input('Pressione enter para continuar.')
            print()
            cont += 1

print(f'\n\n\n{"Programa encerrado    (_　_)。゜zｚＺ":^45}\n')
