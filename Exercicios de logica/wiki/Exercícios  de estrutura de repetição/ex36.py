"""Desenvolva um programa que faça a tabuada de um número
qualquer inteiro que será digitado pelo usuário, mas a
tabuada não deve necessariamente iniciar em 1 e terminar em
10, o valor inicial e final devem ser informados também pelo
usuário, conforme exemplo abaixo:Montar a tabuada de: 5
Começar por: 4 Terminar em: 7 Vou montar a tabuada de 5
começando em 4 e terminando em 7: 5 X 4 = 20 5 X 5 = 25 5
X 6 = 30 5 X 7 = 35Obs: Você deve verificar se o usuário
não digitou o final menor que o inicial."""

while True:  # Enquanto o usuario nao informar todos os numeros necessarios
    while True:  # Enquanto o usuario nao informar o numero que deseja ver a tabuada
        try:
            numero_informado = int(input("\nInforme o numero que deseja ver a tabuada\nNumero: "))
        except:
            print("\n\n\t\t[\033[;31mERRO\033[m]: Informe o numero que deseja ver a tabuada\n")
        else:
            break

    while True:  # Enquanto o usuario nao informar o numero em que a tabuada ira iniciar os calculos
        try:
            comecar_por = int(input("\nInforme o numero que a tabuada ira comecar\nNumero: "))
        except:
            print("\n\n\t\t[\033[;31mERRO\033[m]: Informe o numero que ira comecar na tabuada\n")
        else:
            break

    while True:  # Enquanto o usuario nao informar o numero em que a tabuada ira terminar os calculos
        try:
            terminar_em = int(input("\nInforme o numero em que a tabuada ira terminar\nNumero: "))
        except:
            print("\n\n\t\t[\033[;31mERRO\033[m]: Informe o numero em que a tabuada ira terminar\n")
        else:
            break

    if comecar_por >= terminar_em:  # Se o numero que vai comecar com os calculos for maior do que o numero que termina
        print("\n\n\t\t[\033[;31mERRO\033[m]: O numero em que a tabuada comeca nao pode ser maior que o numero em que a"
              " tabuada termina\n")
    else:
        break

print('\n\n\t\tResultado\n')
for c in range(comecar_por, terminar_em + 1):
    print(f'{c} x {numero_informado} = {c * numero_informado}')
