from enum import Enum  # Importando o metodo enum e o Enum


class Direcoes(Enum):  # Classe que vai herdar do Enum, onde ficara as direcoes possiveis.
    ESQUERDA = 0
    DIREITA = 1
    CIMA = 2
    BAIXO = 3


def mover(direcao):  # Funcao onde ira escrever na tela a direcao escolhida
    if direcao in Direcoes:
        print(f'Indo para {direcao.name}')
    else:
        raise ValueError('Direcao informada nao existe.')


# Direcoes que foram escolhidas
mover(Direcoes.BAIXO)
mover(Direcoes.CIMA)
mover(Direcoes.DIREITA)
mover(Direcoes.ESQUERDA)

