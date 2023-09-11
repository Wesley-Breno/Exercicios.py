from . import menu, mostrar_pessoas, adicionar_pessoas

while True:
    opcao = menu()

    if opcao == 1:  # Se o usuario decidiu mostrar as pessoas cadastradas.
        mostrar_pessoas('pessoas.json')

    elif opcao == 2:  # Se o usuario decidiu adicionar mais pessoas.
        adicionar_pessoas('pessoas.json')

    else:
        print('--' * 17)
        print('Saindo do sistema... Ate logo :)')
        print('--' * 17)
        break
