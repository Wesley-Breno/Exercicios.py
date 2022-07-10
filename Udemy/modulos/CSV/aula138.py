import csv

# Dados que serao adicionados no arquivo
nomes = ['Deisline', 'Djullienne', 'Eliolnai', 'Deiveide']
cidades = ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Brasília']
idades = ['1', '2', '3', '4']

if len(nomes) == len(cidades) == len(idades):  # Se os dados forem do mesmo tamanho.
    with open('dados.csv', 'w+') as file:
        file.write('nomes,estados,idades\n')  # Escrevendo o nome da coluna.
        for i, nome in enumerate(nomes):  # Adicionando cada dado
            file.write(nome + ',' + cidades[i] + ',' + str(idades[i]) + '\n')
else:
    print('\n\n\t\t[\033[;31mERRO\033[m]: Verifique se os dados tem o mesmo tamanho.')

with open('dados.csv', 'r') as file:  # Lendo o arquivo e colocando cada dado em uma lista e convertendo para dicionario
    dados = list(csv.DictReader(file))

for dado in dados:  # Mostrando os dados.
    print()
    print(dado)
