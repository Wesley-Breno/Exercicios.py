# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime    # Importando o biblioteca que vai ajudar a pegar a data atual.

date = datetime.date.today()    # Pegando a data atual.
year = date.strftime('%Y')    # Pegando o ano atual.
encerrar = 0    # Variavel para saber se o usuario deseja encerrar ou nao.


print(f'{"Maiores e menores":^45}')
input('\n\nPressione enter para comecar.\n\n\n\n')

while True:    # Enquanto o usuario nao digitar 0.
    anos = []
    maiores = []
    menores = []
    
    print(f'{"Digite [ 0 ] para encerrar.":^45}\n')
    print('__' * 20)
    for c in range(0, 7):
        anos.append(int(input(f'Digite o ano de nascimento da {c + 1}° pessoa\nAno de nascimento: ')))
        if anos[c] == 0:    # Se o usuario digitar 0.
            encerrar += 1    # A variavel vai receber +1 para o programa compreender que deseja encerrar quando sair do loop for.
            break
    
        if (int(year) - anos[c]) < 18:
            menores.append(anos[c])
        else:
            maiores.append(anos[c])
    
        print()
        
    if encerrar > 0:    # Se encerrar for maior que 0 o programa encerra.
        break
    
    print('\n' * 5)
    print(f"""Temos {len(maiores)} pessoas maiores de 18 anos.
Temos {len(menores)} pessoas menores de 18 anos.""")
    print('__' * 20)
    input('Pressione enter para tentar de novo.\n\n\n\n')

print(f'\n\n\n\n{"Programa encerrado com sucesso":^45}\n\n')
