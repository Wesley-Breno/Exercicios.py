from time import sleep  # Função do modulo time que vai fazer o programa demorar alguns segundos para ser executado.

try:  # Tentando abrir e ler o arquivo
    with open('saudar.txt', 'r+') as file:
        file.read()
except:  # Se o arquivo nao existir
    print(f'\n\nArquivo nao existe\n\n')
    sleep(5)

    print('Criando arquivo', end='')
    for c in range(5):
        print('.', end='')
        sleep(1)

    with open('saudar.txt', 'w+') as file:  # Escrevendo o conteudo do arquivo
        file.write('Ola você ¬_¬')

    print(f'\n\n{"Arquivo criado com sucesso!":^45}\n{"Execute o programa novamente para ver a saudacao":^45}\n\n')
else:  # Escrevendo o conteudo que tem dentro do arquivo
    with open('saudar.txt', 'r+') as file:
        print(f'\n\n{file.read():^45}')
