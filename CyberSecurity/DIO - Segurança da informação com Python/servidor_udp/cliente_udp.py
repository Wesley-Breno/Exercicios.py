import socket

conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Objeto de conexao UDP
print('\n\nConexao socket criada com sucesso!')

host = 'localhost'
porta = 5433
mensagem = 'Ola servidor :)'

try:
    print(f'Cliente: {mensagem}')
    conexao.sendto(mensagem.encode(), (host, 5432))  # Empacotando mensagem e enviando para o host com a porta

    dados, servidor = conexao.recvfrom(4096)  # Recebendo resposta do servidor com 4096 bytes
    dados = dados.decode()  # Desempacotando os dados recebidos para pegar o dados
    print(f'Cliente: {dados}')

finally:
    print('Cliente: Fechando a conexão')
    conexao.close()
