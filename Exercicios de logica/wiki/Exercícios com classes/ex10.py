"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel

Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""


class BombaDeCombustivel:
    def __init__(self):
        self.tipo_combustivel = 'gasolina'
        self.valor_litro = 5
        self.litros_combustivel_disponivel = 600

    def altera_valor_combustivel(self, novo_valor: float):
        self.valor_litro = novo_valor

    def altera_nome_combustivel(self, nome_novo_combustivel: str):
        self.tipo_combustivel = nome_novo_combustivel

    def altera_quantidade_combustivel(self, nova_quantidade_combustivel: float):
        self.litros_combustivel_disponivel = nova_quantidade_combustivel

    def abastecer_por_valor(self, valor_abastecido: float):
        litros_abastecidos = valor_abastecido / self.valor_litro

        if valor_abastecido > 0:
            if self.litros_combustivel_disponivel >= litros_abastecidos:  # Se houver combustivel para abastecer
                print(f'Voce abasteceu R$ {valor_abastecido:.2f}, colocamos {litros_abastecidos:.1f}Ls')
                self.litros_combustivel_disponivel -= litros_abastecidos  # Removendo quantidade de combustivel vendida
            else:
                print('\n\t[ERRO]: Erro ao abastecer o carro, nao temos combustivel suficiente.\n\t')

        else:
            print('\n\t[ERRO]: Informe o valor a ser abastecido corretamente!\n\t')

    def abastecer_por_litro(self, quantidade_combustivel: float):
        valor_abastecido = quantidade_combustivel * self.valor_litro

        if quantidade_combustivel > 0:
            if self.litros_combustivel_disponivel >= quantidade_combustivel:
                print(f'Voce abasteceu {quantidade_combustivel}Ls, o total a pagar é de R$ {valor_abastecido:.2f}')
                self.litros_combustivel_disponivel -= quantidade_combustivel
            else:
                print('\n\t[ERRO]: Erro ao abastecer o carro, nao temos combustivel suficiente.\n\t')

        else:
            print('\n\t[ERRO]: Informe a quantidade de combustivel que quer abastecer corretamente!\n\t')


if __name__ == '__main__':
    posto_shell = BombaDeCombustivel()
    posto_shell.abastecer_por_valor(5)
    posto_shell.abastecer_por_litro(1)
    posto_shell.altera_nome_combustivel('diesel')
    posto_shell.altera_valor_combustivel(4)
    posto_shell.altera_quantidade_combustivel(400)
    print(posto_shell.tipo_combustivel)
    print(posto_shell.valor_litro)
    print(posto_shell.litros_combustivel_disponivel)
