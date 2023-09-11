
import sqlite3


class ManipulaDados:
    """
    Classe que sera responsavel por manipular dados de uma table
    de um banco de dados sem ter que escrever os comandos 1 por 1.
    """
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)  # Chamando o banco de dados
        self.cursor = self.conn.cursor()  # Colocando cursor em uma variavel para manipular o banco

    def inserir(self, nome, peso):
        """
        Metodo que sera responsavel por inserir dados na table 'clientes'
        :param nome: Nome do novo 'cliente'
        :param peso: Peso do 'cliente'
        :return: None
        """

        # Inserindo valores informados ou ignorando se ja existem
        self.cursor.execute(f'INSERT OR IGNORE INTO clientes VALUES (?, ?, ?)',
                            (None, nome, peso))  # None = id (auto-incrementa, por isso None)
        self.conn.commit()  # Dando commit para os dados irem para o banco de dados

    def editar(self, ide, novo_nome, novo_peso):
        """
        Metodo responsavel por modificar/editar um dado do banco de dados.
        :param ide: Identificador do cliente
        :param novo_nome: Novo nome do cliente
        :param novo_peso: Novo peso do cliente
        :return: None
        """

        # Editando o nome e peso do banco de dados com base no ID do cliente, ou ignorando se ja tiver esse valor
        self.cursor.execute(f'UPDATE OR IGNORE clientes SET (nome, peso)=(?, ?) WHERE id=?',
                            (novo_nome, novo_peso, ide))  # Informando novo nome, peso e o ID para saber qual cliente é
        self.conn.commit()

    def excluir(self, ide):
        """
        Metodo para excluir os dados do banco de dados com base no ID informado
        :param ide: ID do conjunto de dados que sera apagado
        :return: None
        """
        self.cursor.execute(f'DELETE FROM clientes WHERE id=?',
                            (ide, ))
        self.conn.commit()

    def listar(self):
        """
        Pegando todos os dados da table 'clientes' e mostrando cada um
        :return: None
        """
        dados = self.cursor.execute('SELECT * FROM clientes')
        for pessoa in dados:
            ide, nome, peso = pessoa
            print(ide, nome, peso)

    def buscar(self, valor):
        """
        Metodo para buscar um peso especifico e mostrar na tela todos
        os clientes que tiver este peso
        :param valor: peso que deseja procurar
        :return: None
        """
        dados = self.cursor.execute('SELECT * FROM clientes WHERE peso LIKE ?',
                                    (valor, ))
        for pessoa in dados:
            print(pessoa)

    def fechar(self):
        """
        Metodo para fechar banco de dados.
        :return: None
        """
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    a = ManipulaDados('banquinho.db')

