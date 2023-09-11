"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
"""


class Carro:
    def __init__(self, kms_por_litro):
        self.kms_por_litro = kms_por_litro
        self.tanque_combustivel = 0

    def andar(self, kms):
        litros_gasto = kms / self.kms_por_litro
        if self.tanque_combustivel >= litros_gasto:
            self.tanque_combustivel -= litros_gasto
            print(f'Andou {kms}Kms')
        else:
            print('O veiculo esta sem gasolina.')

    def obter_gasolina(self):
        print(f'Restante de gasolina no tanque: {self.tanque_combustivel:.1f}')

    def adicionar_gasolina(self, quantidade_litros: float):
        self.tanque_combustivel += quantidade_litros


if __name__ == '__main__':
    carro1 = Carro(15)
    carro1.andar(1)
    carro1.obter_gasolina()
    carro1.adicionar_gasolina(20)
    carro1.andar(15)
    carro1.obter_gasolina()
    carro1.andar(100)
