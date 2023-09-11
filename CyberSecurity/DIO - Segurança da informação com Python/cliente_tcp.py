import socket  # Modulo para fazer o relacionamento com a placa de rede e o SO
import sys  # Modulo para fazer o acesso a interações com o Python


def main():
    try:
        """
        socket.AF_INET
            Estamos passando a informação que estaremos usando o protocolo IP
        socket.SOCK_STREAM
            Informando que iremos usar o protocolo TCP
        0
            Protocolo escolhido que fara a comunicação com o servidor (Protocolo escolhido: TCP)     
        """
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)  # Criando socket com suas especificações

    except socket.error as erro:
        print(f'A conexão falhou\n'
              f'ERRO: {erro}')
        sys.exit()  # Fechando programa

    print('\nSocket criado com sucesso.\n')

    # Recenbendo host/ip e a porta do usuario
    host_alvo = input('Digite o HOST/IP a ser conectado: ')
    porta_alvo = int(input('Digite a porta a ser conectada: '))

    try:
        conexao.connect((host_alvo, porta_alvo))  # Tentando se conectar com host e porta informados

        print(f'\nCliente TCP conectado com sucesso!\n'
              f'Host: {host_alvo}\n'
              f'Porta: {porta_alvo}')
        conexao.shutdown(2)  # Esperando 2 segundos para finalizar a conexão

    except socket.error as erro:
        print(f'\nA conexão com o host "{host_alvo}" e a porta "{porta_alvo}" falhou\n'
              f'ERRO: {erro}')
        sys.exit()  # Fechando programa


if __name__ == "__main__":
    main()
