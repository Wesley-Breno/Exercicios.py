import os  # Importando o modulo OS para fazer a manipulacao de arquivos.
from time import sleep  # Importando modulo time com a funcao sleep para fazer a execucao do programa demorar.

encerrar = 1  # Variavel que se receber 0, o programa encerra.

print('\n\t\t\033[;1m- Encontrar arquivo - \033[m\n\n')
while encerrar != 0:
    pasta = str(input('Digite o caminho da pasta: '))
    arquivo = str(input('Digite o nome do arquivo quer quer achar: ').lower())

    arquivos_encontrados = []  # Todos os arquivos encontrados com o nome informado.
    primeiro_arquivo_encontrado = ''  # Caminho do primeiro arquivo encontrado.
    cont = 0  # Contador para saber se é o primeiro arquivo ou nao.

    try:
        for arq in os.listdir(pasta):  # Colocando em uma lista cada arquivo.
            if arquivo in arq.lower():
                if cont == 0:  # Se for o primeiro arquivo.
                    primeiro_arquivo_encontrado += arq
                    cont += 1

                arquivos_encontrados.append(arq)

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, digite um caminho valido.\n\n')
        sleep(2.5)

    else:
        if len(arquivos_encontrados) > 0:  # Se o programa achou algum arquivo.
            print(f'\n{len(arquivos_encontrados)} arquivos encontrado com "{arquivo.title()}"\n')
            endereco_arquivo = pasta + '/'  # Colocando o caminho do arquivo com um '/'.
            for nome in arquivos_encontrados:

                tamanho = int(os.path.getsize((endereco_arquivo + nome)))  # Pegando o tamanho do arquivo.
                if 1000 <= tamanho < 1000000:  # Se o tamanho do arquivo for em KB.
                    tamanho = tamanho / 1000
                    tamanho = str(int(tamanho)) + 'Kb'

                elif 1000000 <= tamanho < 1000000000:  # Se o tamanho do arquivo for em MB.
                    tamanho = tamanho / 10 ** +6
                    tamanho = str(int(tamanho)) + 'Mb'

                elif 1000000000 <= tamanho < 1000000000000:  # Se o tamanho do arquivo for em GB.
                    tamanho = tamanho / 10 ** +9
                    tamanho = str(int(tamanho)) + 'Gb'

                elif 1000000000000 <= tamanho:  # Se o tamanho do arquivo for em TB.
                    tamanho = tamanho / 10 ** +12
                    tamanho = str(int(tamanho)) + 'Tb'

                else:  # Se arquivo for menor que KB.
                    tamanho = str(int(tamanho)) + 'Bytes'

                print('--' * 35)
                print(f"""Nome do arquivo: {nome}
Endereco do arquivo: {endereco_arquivo + nome}
Tamanho em bytes: {os.path.getsize(endereco_arquivo + nome)}
Tamanho formatado: {tamanho}
Extensao do arquivo: {os.path.splitext((endereco_arquivo + nome))[1]}""")  # Pegando a extensao do arquivo.

            while True:  # Perguntando se quer executar o arquivo.
                print('--' * 20)
                try:
                    deseja = int(input('Deseja abrir o primeiro arquivo encontrado?\n'
                                       '[ 1 ] - Sim\n[ 2 ] - Nao\n\n'
                                       '> '))

                except:
                    print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, digite um valor valido.\n\n')
                    sleep(2.5)

                else:  # Executando o arquivo encontrado.
                    if deseja == 1:
                        os.startfile(pasta + '/' + primeiro_arquivo_encontrado)
                        encerrar = 0
                        break

                    elif deseja == 2:  # Encerrando programa.
                        encerrar = 0
                        break

                    else:
                        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, digite um valor valido.\n\n')
                        sleep(2.5)

        else:  # Se nenhum arquivo foi encontrado.
            print(f'\n\n\t\t\033[;31mNenhum\033[m arquivo encontrado com "{arquivo.title()}"\n\n')

print('\n\n\t\tPrograma encerrado com \033[;32msucesso\033[m :)\n\n')
