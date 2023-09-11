import hashlib

# Nome dos arquivos que serao comparados
arquivo1 = 'msg1.txt'
arquivo2 = 'msg2.txt'

hash1 = hashlib.new('ripemd160')  # Algoritmo que sera usado para fazer o hash
hash1.update(open(arquivo1, 'rb').read())  # Abrindo o arquivo e criando hash

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():  # Se o arquivo msg1.txt for diferente do arquivo msg2.txt
    print(f'Os arquivos são diferentes!\n'
          f'Hash do arquivo "{arquivo1}": {hash1.hexdigest()}\n'
          f'Hash do arquivo "{arquivo2}": {hash2.hexdigest()}')  # Mostrando o hash de cada arquivo
else:
    print(f'Os arquivos são iguais!\n'
          f'Hash do arquivo "{arquivo1}": {hash1.hexdigest()}\n'
          f'Hash do arquivo "{arquivo2}": {hash2.hexdigest()}')
