"""
Faça um Programa que verifique se uma letra digitada é 
"F" ou "M". Conforme a letra escrever: 
F - Feminino, M - Masculino, Sexo Inválido.
"""

while True:  #Enquanto o usuario nao digitar F ou M.
    sexo = str(input('\n\n\t\tDigite o seu sexo\n' \
	                'F - Feminino\n' \
	                'M - Masculino\n\n' \
	                'Seu sexo: ')).upper()

    if sexo == 'F':
        print('\n\n\t\tSeu sexo é feminino\n')
        break

    elif sexo == 'M':
        print('\n\n\t\tSeu sexo é masculino\n')
        break

    else:
        print('\n\n\t\t\033[31;mInforme um dado valido\n\033[m\n')
    
