"""
Usei o mypy para fazer os testes e verificar se ha algo de errado no codigo.
"""

from typing import List, Union, Tuple, Dict, Any, Callable, Sequence, Iterable

# Especificando variaveis com os tipos de valores que elas devem receber.
numero: int = 10
flutuante: float = 1.2
string: str = '1'
booleano: bool = True

# Especificando sequencias e os valores que devem receber.
lista: List[int] = [1, 2, 3]  # Lista que so pode receber valores do tipo int.
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'werlindo']  # Lista que so pode receber valores do tipo str ou int.
tupla: Tuple[int, int, int, str] = (1, 2, 3, '4')  # Tupla so pode receber 4 valores e o seu tipo especifico int ou str.

# Especificando os tipos primitivos das chaves e valores dos dicionarios.
pessoa: Dict[str, Union[str, int]] = {'nome': 'Werlei', 'idade': 12}  # Dicionario que so pode receber chaves que sao do tipo str e valores do tipo str ou int.
pessoa2: Dict[str, Any] = {'nome': 'Werlei', 'idade': 12, 'casado?': False}  # Dicionario que so pode receber chaves que sao do tipo str e qualquer valor de qualquer tipo primitivo.
pessoa3: Dict[str, Union[str, int, List[int]]] = {'nome': 'Werlei', 'idade': 12, 'numeros_preferidos': [1, 2, 3]}  # Dicionario que so pode receber chaves do tipo str e valores do tipo str, int ou lista que so recebe valores do tipo int.


def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    """
    Funcao que recebe uma funcao que os parametros dessa funcao recebida
    devem ser 2 valores do tipo int e retornar um valor do tipo int.

    :param funcao: Parametro que recebera uma funcao e que essa funcao deve
    receber dois parametros de tipo int e retornar um valor int.
    """
    return funcao


def soma(x: int, y: int) -> int:
    """
    Funcao que recebe dois parametros que devem ser do tipo int
    e retorna os valores dos parametros somados.

    :param x: Parametro que sera recebido um valor do tipo int
    :param y: Parametro que sera recebido um valor do tipo int
    :return: Retorna a soma dos valores dos parametros
    """
    return x + y


print(retorna_funcao(soma)(20, 10))  # Chamando funcao que recebe uma funcao, informando parametros da funcao recebida.


class Pessoa:
    """
    Classe so recebe parametros do tipo str, int e atributos do tipo str e int.
    """
    def __init__(self, nome: str, sobrenome: str, idade: int):
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        """
        Funcao que mostra uma mensagem e especificando que ela nao retorna nada (None).
        :return: None
        """
        print(f'{self.nome} {self.sobrenome} esta falando...')


def iterar(sequencia: Sequence[int]):
    """
    Funcao especificada que recebera uma sequencia que os seus valores devem ser do tipo int.
    :param sequencia: Sequencia que sera recebida como parametro.
    :return: Retorna a sequencia com seus valores dobrados.
    """
    return [x * 2 for x in sequencia]


def iterar2(iteravel: Iterable[int]):
    """
    Funcao especificada que recebera um iteravel que os seus valores devem ser do tipo int.
    :param iteravel: Iteravel que sera recebido como parametro.
    :return: Retorna o iteravel com seus valores duplicados.
    """
    return [x * 2 for x in iteravel]


print(iterar([1, 2, 3]))
print(iterar2([1, 2, 3]))
