"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um
levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se
encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número
indeterminado de entradas, cada uma contendo:
um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza;
a.necessita troca do cabo ou conector;
a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa.

Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""

from tabulate import tabulate  # Funcao que sera responsavel por fazer a tabela do resultado

situacao_votos = [0] * 4  # Votos de cada situacao

print('\n\n\t\tDigite 0 (zero) para encerrar o programa\n\n')

# Enquanto o usuario nao digitar zero
while True:
    try:
        print('--' * 27)
        situacao = int(input("""Informe o numero que corresponde a situacao do mouse

1- Necessita da esfera
2- Necessita de limpeza
3- Necessita troca do cabo ou conector
4- Quebrado ou inutilizado

Situacao: """))

    except ValueError:
        print('\n\n\t\t[ERRO]: Informe o numero que corresponde a situacao do mouse\n\n')

    else:
        if situacao == 0:  # Se o usuario decidiu encerrar o programa
            break

        if 0 < situacao <= 4:  # Se o numero que o usuario informou corresponde a algum dos numeros da votacao
            situacao_votos[situacao - 1] += 1

        else:
            print('\n\n\t\t[ERRO]: Informe o numero que corresponde a situacao do mouse\n\n')

    print()

total_mouses_quebrados = sum(situacao_votos)

if total_mouses_quebrados == 0:  # Se o usuario nao informou nenhum mouse com defeito
    print('\n\n\t\tVoce nao informou nenhum mouse com defeito\n\n')

else:
    print(f"\nQuantidade de mouses: {sum(situacao_votos)}")

    # Mostrando na tela o tipo de defeito, a quantidade de mouses com este defeito e o percentual com base nos defeitos
    print(tabulate(
        [
            ['necessita da esfera', situacao_votos[0], f'{situacao_votos[0] / total_mouses_quebrados * 100:.1f}'],
            ['necessita de limpeza', situacao_votos[1], f'{situacao_votos[1] / total_mouses_quebrados * 100:.1f}'],
            ['necessita troca do cabo ou conector', situacao_votos[2], f'{situacao_votos[2] / total_mouses_quebrados * 100:.1f}'],
            ['quebrado ou inutilizado', situacao_votos[3], f'{situacao_votos[3] / total_mouses_quebrados * 100:.1f}'],
         ], headers=['Situacao', 'Quantidade', 'Percentual'], tablefmt='pretty'))
