"""
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos
comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos,
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente
fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""


class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        if type(alimento) == Macaco:
            alimento = 'Macaco ' + alimento.nome

        self.bucho.append(alimento)
        self.ver_bucho()

    def ver_bucho(self):
        print(f'O macaco {self.nome} comeu: {self.bucho.__str__()}')

    def digerir(self):
        self.bucho.clear()


if __name__ == '__main__':
    mamaco1 = Macaco('Adam')
    mamaco2 = Macaco('Sandler')

    mamaco2.comer('Banana')
    mamaco2.comer('Acerola')
    mamaco2.comer('Uva')

    print()

    mamaco1.comer(mamaco2)
    mamaco1.comer('Folha')
    mamaco1.comer('Manga')

    mamaco1.digerir()
    mamaco2.digerir()
