"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
maiores_18, homens, mulheres_menor_20 = 0, 0, 0

print('\n\n\tAdicione pessoas\n\n')

while True:
    print()
    print('--' * 13)
    try:
        idade = int(input('Digite a idade: '))

    except ValueError:
        print('\t\nerro, digite um valor valido')

    else:
        try:
            sexo = str(input('Digite o sexo [M/F]: ').upper())[0]
   
        except IndexError:
            print('\t\nerro, digite F ou M para escolher')
    
        else:
            if sexo == 'F' or sexo == 'M':
                try:
                  quer_continuar = str(input('deseja continuar? [S/N] > ').upper())[0]
            
                except IndexError:
                    print('\t\nerro, digite S ou N para escolher')
           
                else:
                    if quer_continuar == 'S' or quer_continuar == 'N':
                        if idade > 18:
                            maiores_18 += 1
                        if sexo == 'M':
                            homens += 1
                        if idade < 20 and sexo == 'F':
                            mulheres_menor_20 += 1
                        if quer_continuar == 'N':
                            break
                    else:
                        print('\t\nerro, digite S ou N para escolher')
       
            else:
                print('\t\nerro, digite F ou M para escolher')

print(f"""
        Informações
▪︎ Maiores de 18 anos: {maiores_18}
▪︎ Total de homens: {homens}
▪︎ Mulheres menores de 20: {mulheres_menor_20}

""")
