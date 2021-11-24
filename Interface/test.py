# Algoritmo usado para a criacao de uma janela em branco.

import sys  # Para a gente poder interagir com a interface.
from PyQt5.QtWidgets import QApplication, QMainWindow   # Fazer a criacao da janela.


class Janela(QMainWindow):  # Criando o objeto 'janela'.
    def __init__(self):
        super().__init__()  # Coloquei a funcao super() para poder usar o QMainWindow sem nenhum problema.

        # Aqui ficam os atributos da janela, largura, altura e etc.
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = 'Janelona'
        self.CarregarJanela()   
        
    def CarregarJanela(self):   # Funcao que vai fazer mostrar a janela com seus atributos e etc.
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)   # Colocar os atributos 
        self.setWindowTitle(self.titulo)    # Colocar o titulo
        self.show() # Mostrar a janela


aplicacao = QApplication(sys.argv)  # Objeto que sera uma referencia do QApplication
j = Janela()    #   Criando a janela
sys.exit(aplicacao.exec_()) # Interaçao com a interface
