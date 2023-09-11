# Crie um laço de repetição onde do lado esquerdo ira contar
# de 0 ate 9, e do lado esquerdo do 10 ate o 1.

print('\033[;1m|Crescente|\t|Decrescente|\033[m')
for p, n in enumerate(range(10, 1, -1)):  # Fazendo a contagem dos dois lados. usando o enumerate para fazer o crescente e o range para o decrescente.
    print(f'\t{p}\t\t\t{n}')
