# Sistema de perguntas e respostas com dicionarios em Python

perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2+3?',
        'respostas': {
            'a': '5',
            'b': '6',
            'c': '4'
        },
        'resposta_certa': 'a'
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 3x5?',
        'respostas': {
            'a': '10',
            'b': '14',
            'c': '15'
        },
        'resposta_certa': 'c'
    },
    'pergunta 3': {
        'pergunta': 'Quanto é 6/2?',
        'respostas': {
            'a': '2',
            'b': '3',
            'c': '4'
        },
        'resposta_certa': 'b'
    }
}

total_de_acertos, total_de_erros = 0, 0

for p, v in perguntas.items():
    print(p)
    print(v['pergunta'])

    for k, l in v['respostas'].items():
        print(f'[ {k} ] - {l}')

    resposta_usuario = str(input('Digite a resposta: ')).lower()[0]

    if resposta_usuario == v['resposta_certa']:
        print('Você \033[;32mcertou\033[m!!')
        total_de_acertos += 1
    else:
        print('Você \033[;31merrou\033[m!')
        total_de_erros += 1

    print()

print(f'\n\n{"Fim de jogo":^45}\n'
      f'{f"Total de acertos: {total_de_acertos}":^45}\n'
      f'{f"Total de erros: {total_de_erros}":^45}\n'
      f'{f"Porcentagem de acertos: {total_de_acertos / len(perguntas) * 100:.1f}%":^45}')
