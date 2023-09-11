from zipfile import ZipFile  # Classe para ajudar a criar/extrair pastas.zip
from os import path, listdir, removedirs, remove  # Modulo para ajudar a manipular arquivos

print('\n' * 2)
caminho = str(input('Informe o caminho da pasta: '))

if path.isdir(caminho):  # Se for uma pasta comum
    try:

        with ZipFile(caminho + '.zip', 'w') as file:  # Criando a pasta compactada
            for arquivo in listdir(caminho):  # Para cada arquivo na pasta original
                caminho_completo = path.join(caminho, arquivo)  # Pegando o caminho e o nome de cada arquivo
                file.write(caminho_completo, arquivo)  # Pegando arquivo da pasta original, colocando arquivo na...
                # pasta.zip

        for arquivo in listdir(caminho):  # Apagando cada arquivo da pasta original
            remove(path.join(caminho, arquivo))
        removedirs(caminho)  # Apagando pasta original e deixando so a pasta.zip

    except:

        print('\n\n\t[\033[;31mERRO\033[m]: Verifique se o caminho informado é de uma pasta comum.\n\n')

    else:

        print('--' * 20)
        print('Pasta convertida para .zip com \033[;32msucesso\033[m.')

else:  # Se for uma pasta.zip
    try:

        with ZipFile(caminho + '.zip', 'r') as file:  # Pegando arquivos da pasta.zip e criando nova pasta descompactada
            file.extractall(caminho)  # Extraindo todos arquivos

        remove(caminho + '.zip')  # Apagando pasta.zip e deixando somente a pasta descompactada

    except:

        print('\n\n\t[\033[;31mERRO\033[m]: Verifique se o caminho informado é de uma pasta comum.\n\n')

    else:

        print('--' * 16)
        print('Pasta descompactada com \033[;32msucesso\033[m.')
