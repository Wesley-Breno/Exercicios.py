from contas import *  # Importando os tipos de conta e o banco


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    """
    Classe onde ficara o nome e idade da pessoa, e se ela
    tem conta ou nao.
    """
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None
