"""
Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres
embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação
possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa
baixa, independentemente de como foram digitados.
"""
from random import choice


def embaralhador_de_palavra(palavra: str) -> str:
    """
    Funcao que recebe uma palavra (str) como parametro, pega o total de index da palavra,
    e escolhe aleatoriamente os index que serao colocados, gerando assim uma palavra embaralhada e a retornando.
    :param palavra: Palavra do tipo str que sera embaralhada
    :return: Retorna um string com a palavra embaralhada
    """

    # Pegando o total de index que a palavra tem
    total_index = []
    for c in range(0, len(palavra)):
        total_index.append(c)

    # Escolhendo cada index de cada letra aleatoriamente
    letras_escolhidas = []
    while True:  # Enquanto a funcao nao escolher cada index de cada letra de uma forma aleatoria
        escolha = choice(total_index)
        if len(letras_escolhidas) == len(palavra):  # Se o programa escolheu todos os index das letras aleatoriamente
            break
        if escolha not in letras_escolhidas:  # Se o index da letra ainda nao foi escolhido
            letras_escolhidas.append(escolha)

    # Usando os index das letras escolhidas aleatoriamente para gerar a palavra embaralhada
    palavra_embaralhada = ''
    for index_letra in letras_escolhidas:
        palavra_embaralhada += palavra[index_letra]

    return palavra_embaralhada.lower()


if __name__ == '__main__':
    wesley = embaralhador_de_palavra('wesley')
    jose = embaralhador_de_palavra('jose')
    print(wesley)
    print(jose)
