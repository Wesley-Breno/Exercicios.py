"""
Template Method (comportamental) tem a intenção de definir um algoritmo em um metodo, postergando alguns passos para as
subclasses por herança. Template Method permite que subclasses redefinam certos passos de um algoritmo sem mudar a
estrutura do mesmo.

Tambem é possivel definir hooks para que as subclasses utilizem caso necessario.
"""
from abc import ABC, abstractmethod


class Pizza(ABC):
    """  Classe abstrata  """

    def prepare(self):
        """  Template method"""
        self.hook_before_add_ingredients()  # Hook
        self.add_ingrentients()  # Abstract
        self.hook_after_add_ingredients()  # Hook
        self.cook()  # Abstract
        self.cut()  # Concreto
        self.serve()  # Concreto

    def hook_before_add_ingredients(self):
        ...

    def hook_after_add_ingredients(self):
        ...

    def cut(self):
        print(f'{self.__class__.__name__} - Cortando pizza.')

    def serve(self):
        print(f'{self.__class__.__name__} - Servindo pizza.')

    @abstractmethod
    def add_ingrentients(self):
        ...

    @abstractmethod
    def cook(self):
        ...


class AModa(Pizza):
    def add_ingrentients(self):
        print('AModa - adicionando ingredientes: presunto, queijo e goiabada')

    def cook(self):
        print('AModa - Cozinhando por 45min no forno a lenha')


class PizzaVegana(Pizza):
    def hook_before_add_ingredients(self):
        print('PizzaVegana - Lavando os ingredientes')

    def add_ingrentients(self):
        print('PizzaVegana - adicionando ingredientes: ingredientes veganos')

    def cook(self):
        print('PizzaVegana - Cozinhando por 5min no forno comum')


if __name__ == '__main__':
    a_moda = AModa()
    a_moda.prepare()

    print()

    vegana = PizzaVegana()
    vegana.prepare()
