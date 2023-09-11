"""
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir_valores(self):
        print(f'x = {self.x}, y = {self.y}\n')


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def encontrar_centro_do_retangulo(self):
        cordenada_x = self.largura / 2
        cordenada_y = self.altura / 2
        return cordenada_x, cordenada_y


if __name__ == '__main__':
    print('\n\n\t\t[Digite -1 para encerrar]\n\n')

    while True:
        try:
            largura_informada = float(input('Informe a largura do retangulo: '))
            if largura_informada == -1:
                break

            altura_informada = float(input('Informe a altura do retangulo: '))
            if altura_informada == -1:
                break

        except ValueError:
            print('\n\n\t\t[ERRO]: Informe a largura e altura corretamente!\n\n')

        else:
            retangulo = Retangulo(largura_informada, altura_informada)
            x, y = retangulo.encontrar_centro_do_retangulo()
            ponto = Ponto(x, y)
            ponto.imprimir_valores()
