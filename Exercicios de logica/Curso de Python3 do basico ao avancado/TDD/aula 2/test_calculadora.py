"""
Aprendendo a usar o framework unittest
"""


import unittest
from calculadora import soma


class TestCalculadora(unittest.TestCase):
    """
    Classe que sera responsavel por fazer testes na classe soma.
    """

    def test_soma_5_e_5_deve_retornar_10(self):
        """
        Testando se a soma de 5 + 5 vai ser igual a 10
        """
        self.assertEqual(soma(5, 5), 10)  # Chamando funcao e seus parametros e logo em seguida o resultado esperado.

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        """
        Testando se a soma entre -5 + 5 vai ser igual a 0
        """
        self.assertEqual(soma(-5, 5), 0)  # Chamando funcao e seus parametros e logo em seguida o resultado esperado.

    def test_soma_varias_entradas(self):
        """
        Testando varios tipos de entradas usando subtests
        """
        x_y_saidas = (
            (1, 3, 4),  # Soma entre 1 + 3, espera o resultado 4
            (2, 2, 4),  # Soma entre 2 + 2, espera o resultado 4
            (1, 1, 2)  # Soma entre 1 + 1, espera o resultado 2
        )

        for saidas in x_y_saidas:  # Para cada saida esperada
            with self.subTest(saidas=saidas):  # Chamando o subtest para mostrar mais detalhadamente o erro.
                x, y, saida = saidas
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        """
        Fazendo um teste onde o resultado esperado é um AssertError
        """
        with self.assertRaises(AssertionError):
            soma('11', 0)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        """
        Fazendo um teste onde o resultado esperado é um AssertError
        """
        with self.assertRaises(AssertionError):
            soma(11, '0')


if __name__ == '__main__':
    unittest.main(verbosity=2)
