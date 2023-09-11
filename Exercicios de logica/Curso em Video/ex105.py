"""
Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as
seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
"""


def notas(*args, situacao=False):
    """
    -> Funcao que recebe varias notas de um aluno e retorna um
    dicionario com:
        * Quantidade de notas
        * Maior nota
        * Menor nota
        * Media
        * Situacao do aluno

    Se situacao do aluno for True, aparecera se o aluno foi Aprovado,
    esta de recuperacao ou reprovado.

    > Se a media for menor que 5 a situacao sera 'Reprovado'.
    > Se a media for menor que 7 e menor ou igual a 5, a situacao sera 'Recuperacao'.
    > Se a media for igual ou maior que 7, a situacao sera 'Aprovado'.

    :param args: Parametro que recebera as notas
    :param situacao: True: Mostra a situacao do aluno. False: Nao mostra a situacao.
    :return: Retorna um dicionario com as informacoes.
    """

    cont = 0  # Contador para saber se todos os caracteres sao numeros.
    for nota in args:
        if type(nota) == float or type(nota) == int:  # Se o tipo do caractere for Float ou Int.
            cont += 1

    dicionario = dict()
    if cont == len(args):  # Se todos os caracteres forem numeros.
        dicionario['total_notas'] = len(args)
        dicionario['maior_nota'] = max(args)
        dicionario['menor_nota'] = min(args)
        dicionario['media'] = sum(args) / len(args)

        if situacao:  # Se o usuario quiser mostrar a situacao.
            if dicionario['media'] >= 7:
                dicionario['situacao'] = 'Aprovado'

            elif 7 > dicionario['media'] >= 5:
                dicionario['situacao'] = 'Recuperacao'

            else:
                dicionario['situacao'] = 'Reprovado'

    dicionario['media'] = f'{dicionario["media"]:.2f}'  # Fazendo a media ter apenas 2 numeros decimais.

    return dicionario


if __name__ == '__main__':
    resp = notas(5.5, 9.5, 10, 6.5, situacao=True)
    print(resp)
