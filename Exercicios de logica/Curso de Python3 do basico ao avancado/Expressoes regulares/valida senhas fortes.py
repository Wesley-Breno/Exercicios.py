
import re

senha = str(input("""
\t\tVerificador de senha forte

Digite a senha: """))

inclui_maiuscula = re.findall(r'[A-Z]+', senha)  # Pegando todas as letras maiusculas
inclui_minuscula = re.findall(r'[a-z]+', senha)  # Pegando todas as letras minusculas
inclui_numeros = re.findall(r'[0-9]+', senha)  # Pegando todos os numeros
inclui_caracteres_especiais = re.findall(r'[!@#$%&*_]+', senha)  # Pegando os caracteres especiais

if len(senha) >= 9:  # Se a senha tiver mais de 9 caracteres
    if len(inclui_maiuscula) >= 1 and len(inclui_minuscula) >= 1 and len(inclui_numeros) >= 1 and \
            len(inclui_caracteres_especiais) >= 1:  # Se a senha tiver todos os requisitos de uma senha forte
        print("""\n\n\t\tSua senha esta \033[1;32mforte\033[m

[✔] Inclui letras maiusculas
[✔] Inclui letras minusculas
[✔] Inclui numeros
[✔] Inclui caracteres especiais
[✔] Tem mais de 9 caracteres""")

    else:
        print("""\n\n\t\tSua senha nao esta \033[1;31mforte\033[m

Tente incluir:

* Letras maiusculas
* Letras minusculas
* Numeros
* Caracteres especiais [!@#$%&*_] 
* Colocar mais de 9 caracteres""")

else:
    print("""\n\n\t\tSua senha nao esta \033[1;31mforte\033[m

Tente incluir:

* Letras maiusculas
* Letras minusculas
* Numeros
* Caracteres especiais [!@#$%&*_] 
* Colocar mais de 9 caracteres""")
