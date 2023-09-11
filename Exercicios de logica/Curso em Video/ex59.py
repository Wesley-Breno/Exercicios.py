from time import sleep  # Importando função para fazer o programa esperar alguns segundos antes de continuar o algoritmo


class OperacoesAritmeticas:  # Classe onde ficara as operacoes aritmeticas
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def somar_numeros(self):
        print(f'\nA soma entre {self.numero1} e {self.numero2} equivale a: \033[;1m{self.numero1 + self.numero2}\033[m')

    def multiplicar_numeros(self):
        print(f'\nA multiplicação entre {self.numero1} e {self.numero2} equivale a: '
              f'\033[;1m{self.numero1 * self.numero2}\033[m')

    def maior_numero(self):
        if self.numero1 == self.numero2:
            print('\n\tOs numeros sao iguais!')
            return

        print(f'\nO maior numero entre {self.numero1} e {self.numero2} é: '
              f'\033[;1m{max(self.numero1, self.numero2)}\033[m')


print()
numeros_lista = []

while len(numeros_lista) != 2:  # Enquanto o usuario nao digitar 2 numeros
    try:
        for c in range(2):
            numeros_lista.append(int(input(f'Digite o {c + 1}° numero: ')))

    except:
        numeros_lista = []  # Esvaziando a lista para adicionar novamente
        print('\n\n\n\033[1;31mERRO\033[m\nPor favor, digite os numeros corretamente.\n\n\n')

    else:
        numeros = OperacoesAritmeticas(numeros_lista[0], numeros_lista[1])  # Adicionando os dois numeros na classe

while True:

    try:
        escolha_menu = int(input("""\n\n\n\n\n
            Escolha oque deseja fazer com os numeros

[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Saber o maior
[ 4 ] - Escolher outros numeros
[ 5 ] - Sair do programa

Escolha: """))

    except:
        print('\n\n\n\033[1;31mERRO\033[m\nPor favor, digite os numeros corretamente.\n\n\n')
        sleep(4.5)

    else:
        if escolha_menu == 1:  # Somar numeros
            numeros.somar_numeros()

        elif escolha_menu == 2:  # Multiplicar numeros
            numeros.multiplicar_numeros()

        elif escolha_menu == 3:  # Ver qual é o maior numero
            numeros.maior_numero()

        elif escolha_menu == 4:  # Trocando os numeros
            print('\nNovos numeros...')
            numeros_lista = []

            while len(numeros_lista) != 2:
                try:
                    for c in range(2):
                        numeros_lista.append(int(input(f'Digite o {c + 1}° numero: ')))
                except:
                    numeros_lista = []
                    print('\n\n\n\033[1;31mERRO\033[m\nPor favor, digite os numeros corretamente.\n\n\n')
                else:
                    numeros = OperacoesAritmeticas(numeros_lista[0], numeros_lista[1])
            print('\n\n\t\tNumeros trocados!')

        elif escolha_menu == 5:  # Encerrando programa
            break

        else:
            print('\n\n\n\033[1;31mERRO\033[m\nPor favor, digite os numeros corretamente.\n\n\n')

        print('__' * 17)
        input('Pressione enter para continuar.')

print('\n\n\n\t\t\tPrograma encerrado :)\n')
