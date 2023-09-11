import socket

conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Obejeto de conexão (Protocolo IP, Conexao tipo UDP)

print('Socket criado com sucesso.')

host = 'localhost'
port = 5432

conexao.bind((host, port))  # Ligacao entre cliente e servidor com base no host e porta
mensagem = '\nServidor: Olaaaaaa cliente :D'  # Mensagem que o servidor ira mandar para o cliente

while 1:  # Enquanto houver conexao com o cliente
    dados, endereco = conexao.recvfrom(4096)  # Recebendo 4096 bytes do endereco da conexao e guardando dentro de dados

    if dados:  # Se o servidor recebeu dados do cliente
        print('Servidor enviando mensagem...')
        conexao.sendto(dados + (mensagem.encode()), endereco)  # Enviando mensagem para cliente UDP
