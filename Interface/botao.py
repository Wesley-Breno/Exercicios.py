import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.altura = 600
        self.largura = 800
        self.titulo = 'Janela'

        botao1 = QPushButton('Botao1', self)    # Criando o primeiro botao e botando seu nome e em seguida o self
        botao1.move(250, 250)   # Colocando a altura e a largura que o botao estara na tela
        botao1.resize(100, 50)  # Colocando a altura e a largura do botao
        botao1.setStyleSheet('QPushButton {background-color:pink; font:bold;}')  # Personalizando o botao com o setStyleSheet com comandos do CSS3
        botao1.clicked.connect(self.botao1_click)   # Caso o botao seja clicado ele ira chamar o metodo 'botao1_click'

        # Criaçao do segundo botao
        botao2 = QPushButton('Botao2', self)
        botao2.move(450, 250)
        botao2.resize(100, 50)
        botao2.setStyleSheet('QPushButton {background-color:pink; font:bold;}')
        botao2.clicked.connect(self.botao2_click)
        self.CarregarJanela()

    # Se o botao 1 for clicado ira printar a mensagem no terminal
    def botao1_click(self):
        print('Botao 1 foi clicado com sucesso.')

    # Se o botao 2 for clicado ira printar a mensagem no terminal
    def botao2_click(self):
        print('Botao 2 foi clicado com sucesso.')

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()


aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
