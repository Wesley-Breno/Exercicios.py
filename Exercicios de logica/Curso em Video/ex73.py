"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

# Os 20 primeiros times da Tabela do Campeonato Brasileiro de Futebol.
tupla_dos_20_times = ('Palmeiras', 'Corinthians', 'Atlético-MG',
                      'Fluminense', 'Athletico-PR', 'Internacional',
                      'São Paulo', 'Santos', 'Flamengo', 'Botaogo',
                      'Bragantino', 'Goiás', 'Cuiabá', 'Coritiba',
                      'América-MG', 'Avaí', 'Ceará SC', 'Atlético-GO',
                      'Juventude', 'Fortaleza')

print('\n\n\t\tCampeonato Brasileiro de Futebol\n\n')

print()
print('__' * 24)
print('Os 5 primeiros times:\n')
for index, time in enumerate(tupla_dos_20_times):  # Mostrando os 5 primeiros times.
    if index < 5:
        print(f'\t{index + 1} - {time}')

cont = 20  # Contador para mostrar a classificacao do lado dos ultimos times.
print()
print('__' * 24)
print('Os ultimos 4 colocados:\n')
for index, time in enumerate(tupla_dos_20_times):
    if index < 5 and index != 0:
        print(f'\t{cont} - {tupla_dos_20_times[-index]}')
        cont -= 1

cont = 3  # Contador para escrever 3 times em uma linha e depois pular de linha.
print()
print('__' * 24)
print('Times em ordem alfabetica:\n')
for time in sorted(tupla_dos_20_times):
    if cont != 0:  # Se o programa ainda nao escreveu 3 times em uma linha.
        print(time, end=' - ')
        cont -= 1
    else:
        print(time)
        cont += 3

print()
print('__' * 24)
print('Posicao do time da Chapecoense:\n')
posicao = ''  # Variavel onde vai ficar a posicao e o nome do time chapecoense, se ele estiver na lista.
for index, time in enumerate(tupla_dos_20_times):
    if time == 'Chapecoense':  # Se um dos times for chapecoense.
        posicao += f'{index + 1} - {time}'

if posicao == '':
    print('\n\t\tO time da Chapecoense nao esta na lista :(\n\n')

else:
    print(posicao)
