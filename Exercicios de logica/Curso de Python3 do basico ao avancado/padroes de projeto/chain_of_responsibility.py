"""
Chain of responsibility (COR) é um padrão comportamental que tem a intenção de evitar o acoplamento do remetente de uma
solicitação ao seu receptor, ao dar a mais de um objeto a oportunidade de tratar a solicitação.

Encadear os objetos receptores passando a solicitação ao longo da cadeia ate que um objeto a trate.
"""

from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str:
        ...


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['A', 'B', 'C']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'Handler_ABC: conseguiu tratar o valor {letter}'

        return self.sucessor.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['D', 'E', 'F']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'Handler_DEF: conseguiu tratar o valor {letter}'

        return self.sucessor.handle(letter)


class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f'Handler_Unsolved: Nao foi possivel tratar {letter}'


if __name__ == '__main__':
    handler_unsolved = HandlerUnsolved()
    handler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)

    print(handler_abc.handle('A'))
    print(handler_abc.handle('B'))
    print(handler_abc.handle('C'))
    print(handler_abc.handle('D'))
    print(handler_abc.handle('E'))
    print(handler_abc.handle('F'))
    print(handler_abc.handle('G'))
    print(handler_abc.handle('H'))
