import os
from PIL import Image


def redimensionar(caminho_da_imagem, largura, altura):
    """
    Funcao que altera a largura e altura de uma imagem.
    ( Lembre-se que apos executar o programa, o arquivo sera substituido. )

    :param caminho_da_imagem: Caminho completo do arquivo.png
    :param largura: Informar a nova largura
    :param altura: Informar a nova altura
    :return: None
    """

    substituir = str(input('\n\tSubstituir foto?\n'
                           '[1] - Sim\n'
                           '[2] - Nao\n'
                           '\n> '))

    if substituir == '1':  # Se o usuario decidiu substituir o arquivo
        if os.path.splitext(caminho_da_imagem)[1] == '.png' and os.path.isfile(caminho_da_imagem):  # Se o caminho informado tiver a extensao '.png' e for um arquivo.
            imagem = Image.open(caminho_da_imagem)  # Abrindo a imagem

            nova_imagem = imagem.resize((largura, altura))  # Colocando a nova altura e nova largura
            nova_imagem.save(
                caminho_da_imagem,  # Informando onde salvar e nome do arquivo
                optimize=True,  # Otimizar a foto
                quality=100  # Qualidade da foto, vai de 1 a 100.
            )

            nova_imagem.close()  # Fechando arquivos
            imagem.close()

        else:
            print('\n\n\t\t\033[;31mArquivo nao encontrado\033[m\n\n')

    elif substituir == '2':  # Se o usuario decidiu criar um novo arquivo com o tamanho informado
        if os.path.splitext(caminho_da_imagem)[1] == '.png' and os.path.isfile(caminho_da_imagem):  # Se o caminho informado tiver a extensao '.png' e for um arquivo.
            nome_arquivo_novo = str(input('\nDigite o nome do novo arquivo: '))

            arquivo_novo = os.path.dirname(caminho_da_imagem) + rf'\{nome_arquivo_novo}.png'  # Pegando o caminho e colocando o nome do novo arquivo
            imagem = Image.open(caminho_da_imagem)  # Abrindo a imagem

            nova_imagem = imagem.resize((largura, altura))  # Colocando a nova altura e nova largura
            nova_imagem.save(
                arquivo_novo,  # Informando onde salvar e nome do arquivo
                optimize=True,  # Otimizar a foto
                quality=100  # Qualidade da foto, vai de 1 a 100.
            )

            nova_imagem.close()  # Fechando arquivos
            imagem.close()

        else:
            print('\n\n\t\t\033[;31mArquivo nao encontrado\033[m\n\n')

    else:
        raise ValueError('Digite apenas [1] para Sim ou [2] para Nao.')

    print('\n\n\t\tArquivo alterado com sucesso.\n\n')


redimensionar(r'C:\Users\jaosd\OneDrive\Imagens\pasta\ui11.png', 600, 600)
