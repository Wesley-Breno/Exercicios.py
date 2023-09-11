import hashlib  # Biblioteca para gerar um hash

while True:  # Enquanto o usuario nao informar o dado a ser gerado o hash e o tipo de hash...
    try:
        # Perguntando o dado que sera gerado o hash e o tipo de hash
        dado = str(input('Informe o dado que deseja gerar o seu hash...\nDado: '))
        tipo_hash = int(input("""
Informe o numero com base no tipo de hash que deseja gerar
[ 1 ] - MD5
[ 2 ] - SHA-1
[ 3 ] - SHA-224
[ 4 ] - SHA-512
[ 5 ] - SHA-256

Tipo de hash: """))
    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe os dados corretamente.\n\n')

    else:
        if tipo_hash == 1:
            nome_hash = 'MD5'
            hash_objeto = hashlib.md5()  # Criando objeto hash e o tipo de hash
            break

        elif tipo_hash == 2:
            nome_hash = 'SHA-1'
            hash_objeto = hashlib.sha1()
            break

        elif tipo_hash == 3:
            nome_hash = 'SHA-224'
            hash_objeto = hashlib.sha224()
            break

        elif tipo_hash == 4:
            nome_hash = 'SHA-512'
            hash_objeto = hashlib.sha512()
            break

        elif tipo_hash == 5:
            nome_hash = 'SHA-256'
            hash_objeto = hashlib.sha256()
            break

        else:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Informe o numero que corresponde ao hash que deseja gerar.\n\n')

dado_bytes = dado.encode()  # Transformando o dado em bytes

hash_objeto.update(dado_bytes)  # Informando o dado que sera gerado o hash
hash = hash_objeto.hexdigest()  # Gerando o hash do dado

print(f'\nDado: {dado}\n'
      f'Hash {nome_hash}: {hash}')
