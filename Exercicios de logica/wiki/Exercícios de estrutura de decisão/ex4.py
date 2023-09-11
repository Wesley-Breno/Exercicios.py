"""
Faça um Programa que verifique se uma letra digitada é 
vogal ou consoante.
"""

vogais = ['A', 'E', 'I', 'O', 'U']
consoantes = ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z'] 

while True:
    try:
        letras = str(input('Digite a letra: '))[0].upper()
    
    except:
        print('\n\n\t\t\033[;31mDigite uma letra.\033[m\n')
    
    else:
        if letras.isdigit():
            print('\n\n\t\t\033[;31mDigite uma letra.\033[m\n')
       
        else:
            break
        
if letras in vogais:
    print(f'\n\n\t\tA letra {letras} é uma vogal\n')
        
else:
    print(f'\n\n\t\tA letra e {letras} é uma consoante\n')
