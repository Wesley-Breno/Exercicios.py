# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

from functions import titulo, pular, press_enter, encerrar, programa_encerrado, erro
from time import sleep


deseja = 0
while deseja != 1:
    total = {'letra a': 0, 'letra e': 0, 'letra i': 0, 'letra o': 0, 'letra u': 0}  # Total de letras de cada vogal
    titulo('Analisador')
    try:
        frase = str(input('Digite uma frase para ser analisada...\nFrase: ').strip().upper())
    except:
        erro('Por favor, tente novamente.')
    else:
        frase_lista = frase.split()
        frase_junto = ''.join(frase_lista)  # Retirando os espaços e deixando tudo junto
        if frase_junto.isalpha():   # Se so tiver letra
            for l in frase:     # Contando as vogais
                if l in 'A':
                    total['letra a'] += 1
                elif l == 'E':
                    total['letra e'] += 1
                elif l == 'I':
                    total['letra i'] += 1
                elif l == 'O':
                    total['letra o'] += 1
                elif l == 'U':
                    total['letra u'] += 1
            pular(5)
            print('--' * 20)
            print(f'''Total de letras na frase \033[1;31m➤\033[m {len(frase_junto)}
----------------------------------------
\033[;1mLETRA A\033[m
Total de letras A \033[1;31m➤\033[m {total['letra a']}
Posicao inicial \033[1;31m➤\033[m {frase.find('A') + 1}
Posicao final \033[1;31m➤\033[m {frase.rfind('A') + 1}
----------------------------------------''')  # .find/.rfind Pegando a primeira e ultima posicao da vogal
            sleep(0.5)  # Fazendo o programa "dormir" por 0.5 segundos para poder executar o restante do codigo
            print(f'''\033[;1mLETRA E\033[m
Total de letras E \033[1;31m➤\033[m {total['letra e']}
Posicao inicial \033[1;31m➤\033[m {frase.find('E') + 1}
Posicao final \033[1;31m➤\033[m {frase.rfind('E') + 1}
----------------------------------------''')
            sleep(0.5)
            print(f'''\033[;1mLETRA I\033[m
Total de letras I \033[1;31m➤\033[m {total['letra i']}
Posicao inicial \033[1;31m➤\033[m {frase.find('I') + 1}
Posicao final \033[1;31m➤\033[m {frase.rfind('I') + 1}
----------------------------------------''')
            sleep(0.5)
            print(f'''\033[;1mLETRA O\033[m
Total de letras O \033[1;31m➤\033[m {total['letra o']}
Posicao inicial \033[1;31m➤\033[m {frase.find('O') + 1}
Posicao final \033[1;31m➤\033[m {frase.rfind('O') + 1}
----------------------------------------''')
            sleep(0.5)
            print(f'''\033[;1mLETRA U\033[m
Total de letras U \033[1;31m➤\033[m {total['letra u']}
Posicao inicial \033[1;31m➤\033[m {frase.find('U') + 1}
Posicao final \033[1;31m➤\033[m {frase.rfind('U') + 1}''')
            print('--' * 20)
            press_enter()   # Mensagem para pressionar enter para poder continuar o programa.
            deseja = encerrar()     # Retorna 1 se o usuario quiser encerrar
            if deseja == 0:     # Se o usuario nao quiser encerrar, pular 5 linhas
                pular(5)
        else:
            erro('Não é permitido o uso de nu-\nmeros e caracteres especiais.')

programa_encerrado()
