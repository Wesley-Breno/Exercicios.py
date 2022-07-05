import os
from time import sleep

encerrar = 1
print('\n\t\t\033[;1m- Encontrar arquivo - \033[m\n\n')
while encerrar != 0:
    pasta = str(input('Digite o caminho da pasta: '))
    arquivo = str(input('Digite o nome do arquivo quer quer achar: ').lower())

    arquivos_encontrados = []
    primeiro_arquivo_encontrado = ''
    cont = 0

    try:
        for arq in os.listdir(pasta):
            if arquivo in arq.lower():
                if cont == 0:
                    primeiro_arquivo_encontrado += arq
                    cont += 1

                arquivos_encontrados.append(arq)

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, digite um caminho valido.\n\n')
        sleep(2.5)

    else:
        if len(arquivos_encontrados) > 0:
            print(f'\n{len(arquivos_encontrados)} arquivos encontrado com "{arquivo.title()}"\n')
            endereco_arquivo = pasta + '/'
            for nome in arquivos_encontrados:

                tamanho = int(os.path.getsize((endereco_arquivo + nome)))
                if 1000 <= tamanho < 1000000:
                    tamanho = tamanho / 1000
                    tamanho = str(int(tamanho)) + 'Kb'

                elif 1000000 <= tamanho < 1000000000:
                    tamanho = tamanho / 10 ** +6
                    tamanho = str(int(tamanho)) + 'Mb'

                elif 1000000000 <= tamanho < 1000000000000:
                    tamanho = tamanho / 10 ** +9
                    tamanho = str(int(tamanho)) + 'Gb'

                elif 1000000000000 <= tamanho:
                    tamanho = tamanho / 10 ** +12
                    tamanho = str(int(tamanho)) + 'Tb'

                else:
                    tamanho = str(int(tamanho)) + 'Bytes'

                print('--' * 35)
                print(f"""Nome do arquivo: {nome}
Endereco do arquivo: {endereco_arquivo + nome}
Tamanho em bytes: {os.path.getsize(endereco_arquivo + nome)}
Tamanho formatado: {tamanho}
Extensao do arquivo: {os.path.splitext((endereco_arquivo + nome))[1]}""")

            while True:
                print('--' * 20)
                try:
                    deseja = int(input('Deseja abrir o primeiro arquivo encontrado?\n'
                                       '[ 1 ] - Sim\n[ 2 ] - Nao\n\n'
                                       '> '))

                except:
                    print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, digite um valor valido.\n\n')
                    sleep(2.5)

                else:
                    if deseja == 1:
                        os.startfile(pasta + '/' + primeiro_arquivo_encontrado)
                        encerrar = 0
                        break

                    elif deseja == 2:
                        encerrar = 0
                        break

                    else:
                        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, digite um valor valido.\n\n')
                        sleep(2.5)

        else:
            print(f'\n\n\t\t\033[;31mNenhum\033[m arquivo encontrado com "{arquivo.title()}"\n\n')

print('\n\n\t\tPrograma encerrado com \033[;32msucesso\033[m :)\n\n')
