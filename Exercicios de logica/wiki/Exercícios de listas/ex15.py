"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

* Mostre a quantidade de valores que foram lidos;
* Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
* Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
* Calcule e mostre a soma dos valores;
* Calcule e mostre a média dos valores;
* Calcule e mostre a quantidade de valores acima da média calculada;
* Calcule e mostre a quantidade de valores abaixo de sete;
* Encerre o programa com uma mensagem;
"""

from time import sleep  # Chamando funcao para fazer o programar demorar para executar o proximo comando

notas = []
cont = 1  # Contador que ira informar qual nota o usuario esta informando

print('\n\n\t\t\033[;37mDigite [ -1 ] para parar de adicionar notas\033[m\n')

while True:  # Enquanto o usuario nao informar -1 para parar de adicionar notas
    try:
        print()
        print('__' * 10)
        nota = float(input(f'Informe a {cont}º nota\nNota: '))

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe a nota corretamente.\n\n')

    else:
        if nota == -1:  # Se o usuario decidiu parar de adicionar notas
            break

        notas.append(nota)
        cont += 1

if len(notas) > 0:  # Se o usuario informou pelo menos uma nota
    quantidade_valores_acima_da_media = 0
    quantidade_valores_abaixo_de_7 = 0

    for nota in notas:
        if nota > (sum(notas) / len(notas)):  # Se a nota informada for maior que a media das notas
            quantidade_valores_acima_da_media += 1

        if nota < 7:
            quantidade_valores_abaixo_de_7 += 1

    print(f"""
        RESULTADO

* Quantidade de notas informadas: {len(notas)}
* Notas informadas: {notas}
* Notas informadas em ordem inversa ↴""")

    for nota in range(len(notas) - 1, -1, -1):  # Mostrando notas na ordem inversa, uma abaixo da outra.
        print(f'\t\t{notas[nota]}')

    print(f"""* Soma das notas: {sum(notas)}
* Media das notas: {sum(notas) / len(notas):.1f}
* Quantidade de valores acima da media: {quantidade_valores_acima_da_media}
* Quantidade de valores abaixo de 7: {quantidade_valores_abaixo_de_7}""")

else:
    print('\n\n\t\t\033[;37mVoce nao adicionou nenhuma nota\033[m\n\n')

sleep(2)  # Esperando 2 segundos para executar o proximo comando
print('\n\n\t\t\033[;37mPrograma encerrado, ate logo!\033[m\n\n')
