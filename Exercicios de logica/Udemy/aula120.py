class Meta(type):  # MetaClasse
    def __new__(mcs, name, bases, namespace):  # name = nome da classe/subclasse, bases = metodos bases da classe/subclasse, namespace = nomes dos atributos e metodos.
        if name == 'A':  # Se for classe
            return type.__new__(mcs, name, bases, namespace)  # Retornando os valores da classe A para SubClasse B

        if 'b_fala' not in namespace:  # Se nao tiver esse atributo/metodo em SubClasse
            print(f'Voce precisa criar a funçao "b_fala" na classe {name}')
        else:
            if not callable(namespace['b_fala']):  # Se nao for um metodo
                print(f'"b_fala" precisa ser um metodo, nao um atributo em {name}')
        return type.__new__(mcs, name, bases, namespace)  # Retornando valores da SubClasse


class A(metaclass=Meta):  # Classe
    def fala(self):
        self.b_fala()


class B(A):  # SubClasse
    b_fala = 'a'
