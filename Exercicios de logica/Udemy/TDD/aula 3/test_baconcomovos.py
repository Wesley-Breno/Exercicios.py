"""
TDD - Test driven development (Desenvolvimento dirigido a testes)

RED
Parte 1 - Criar o teste e ver falhar

GREEN
Parte 2 - Criar o codigo e ver o teste passar

REFACTOR
Parte 3 - Melhorar o codigo
"""

import unittest
from baconcomovos import bacon_com_ovos  # Importando funcao que foi criada


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_dar_assertionerror_se_nao_receber_int(self):
        """
        Testando a funcao bacon_com_ovos para ver se eu mandar
        uma string a funcao ira retornar um assertionerror.
        """

        with self.assertRaises(AssertionError):  # Informando que quero que a função retorne uma AssertionError
            bacon_com_ovos('a')  # Chamando função e colocando seu parametro.

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        """
        Testando a funcao bacon_com_ovos para ver se os numeros
        colocados como entrada retornam 'bacon com ovos', ja que
        se o numero for multiplo de 3 e 5, a funcao deve retornar 'bacon com ovos'.
        """

        entradas = (15, 30, 45, 60)  # Numeros que serao usados no teste.
        saida = 'Bacon com ovos'  # Valor esperado que a funcao retorne.

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):  # Chamando o subtest e informando as variaveis.
                self.assertEqual(bacon_com_ovos(entrada),  # Chamando funcao e informando a entrada da vez.
                                 saida,  # Informando o retorno esperado.
                                 msg=f'{entrada} nao retornou {saida}')  # Mensagem que aparecera caso o teste nao tenha o retorno esperado.

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        """
        Testando a funcao para ver se as entradas informadas retornam
        'passar fome', ja que se o numero informado como parametro nao
        for um multiplo de 3 ou 5, a funcao retornara 'passar fome'.
        """
        entradas = (1, 2, 7, 8)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'{entrada} nao retornou {saida}')

    def test_bacon_com_ovos_deve_retornar_bacon(self):
        """
        Testando as entradas informadas para ver se a funcao retorna
        'bacon' se o numero informado no parametro for apenas multiplo de 3.
        """
        entradas = (6, 12, 18, 24)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'{entrada} nao retornou {saida}')

    def test_bacon_com_ovos_deve_retornar_ovos(self):
        """
        Testando as entradas informadas para ver se a funcao retorna
        'ovos' se o numero informado no parametro for apenas multiplo de 5.
        """
        entradas = (5, 10, 25, 35)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'{entrada} nao retornou {saida}')


if __name__ == '__main__':
    unittest.main(verbosity=2)  # Iniciando teste.
