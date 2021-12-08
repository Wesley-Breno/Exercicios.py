# Crie um laço de repetição onde do lado esquerdo ira contar
# de 0 ate 9, e do lado esquerdo do 10 ate o 1.

contador_crescente = 0
contador_decrescente = 10

for c in range(0, 3):   # Fazer pular 4 linhas
    print()

print('\033[;1m|Crescente|\t|Decrescente|\033[m')
for c in range(0, 10):  # Fazendo a contagem dos dois lados.
    print(f'\t{contador_crescente}\t\t\t{contador_decrescente}')
    contador_crescente += 1
    contador_decrescente -= 1
