class Eletronico:  # Classe pai
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def power(self):  # Metodo para ligar se estiver desligado e vice-versa.
        if not self._ligado:
            self._ligado = True
            print(f'{self._nome} [ \033[1;32mOn\033[m ]')
            return

        self._ligado = False
        print(f'{self._nome} [ \033[1;31mOff\033[m ]')
