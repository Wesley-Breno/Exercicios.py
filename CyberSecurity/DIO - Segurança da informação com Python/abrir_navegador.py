import webbrowser  # Biblioteca responsavel por abrir o navegador
from tkinter import *  # Biblioteca responsavel por fazer a interface do usuario

root = Tk( )  # Objeto que sera representado pela interface

root.title('Abrir navegador')  # Titulo da janela da interface
root.geometry('300x200')  # Tamanho da janela


def google():  # Função que abre o navegador no site da google
    webbrowser.open('www.google.com')


# Botao que ao ser pressionado ira ir para o site da google
my_google = Button(root, text='Abrir google', command=google).pack(pady=20)
root.mainloop()  # Rodando a interface do usuario
