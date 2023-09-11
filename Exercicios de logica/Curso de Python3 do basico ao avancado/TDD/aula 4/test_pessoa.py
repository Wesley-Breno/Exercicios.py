"""
class Pessoa  # Testar a classe Pessoa()
    __init__
        nome str  # Testar se a variavel nome retorna um valor do tipo str.
        sobrenome str  # Testar se a variavel sobrenome retorna um valor do tipo str.
        dados_obtidos bool  # Testar se a classe recebe um valor booleano

    API:
        obter_todos_os_dados -> method
            OK
            404

            (dados_obtidos recebe True se for OK)

"""

import unittest
from unittest.mock import patch
from pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    """
    Classe que testa os retornos de uma classe.
    """
    def setUp(self):
        """
        Funcao que cria objetos com seus parametros, para
        nao ter que ficar criando o objeto a cada teste feito.
        """
        self.p1 = Pessoa('Wesley', 'Breno')  # Criando objeto p1 com nome e sobrenome
        self.p2 = Pessoa('Marisa', 'Rates')  # Criando objeto p2 com nome e sobrenome

    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        """
        Testando para ver se o parametro nome dos objetos p1 e p2
        tem o valor esperado.
        """
        self.assertEqual(self.p1.nome, 'Wesley')
        self.assertEqual(self.p2.nome, 'Marisa')

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        """
        Testando para ver se o parametro sobrenome dos objetos p1 e p2
        tem o valor esperado.
        """
        self.assertEqual(self.p1.sobrenome, 'Breno')
        self.assertEqual(self.p2.sobrenome, 'Rates')

    def test_pessoa_attr_nome_tem_instancia_str(self):
        """
        Testando para ver se o tipo do parametro nome
        dos objetos p1 e p2 sao str.
        """
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)

    def test_pessoa_attr_sobrenome_tem_instancia_str(self):
        """
        Testando para ver se o tipo do parametro sobrenome
        dos objetos p1 e p2 sao str.
        """
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_com_false(self):
        """
        Testando para ver se a variavel dados_obtidos dos
        objetos p1 e p2 comecam como False.
        """
        self.assertFalse(self.p1.dados_obtidos)
        self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_OK(self):
        """
        Testando para ver se o teste consegue usar o metodo
        obter_todos_os_dados com o uso do modulo requests e
        esperar que o metodo retorne 'CONECTADO' e variavel
        dados_obtidos seja igual a True.
        """
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        """
        Testando para ver se o teste consegue usar o metodo
        obter_todos_os_dados com o uso do modulo requests e
        esperar que o metodo retorne 'ERRO 404' e a variavel
        dados_obtidos seja igual a False.
        """
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        """
        Testando para ver se o teste consegue usar o metodo
        obter_todos_os_dados com o uso do modulo requests em
        dois objetos e esperar que o modulo do objeto retorne
        'CONECTADO' no metodo dos dois objeto e em seguida 'ERRO 404'.
        """
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p2.dados_obtidos)


if __name__ == '__main__':
    unittest.main(verbosity=2)
