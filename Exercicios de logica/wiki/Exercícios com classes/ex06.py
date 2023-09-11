"""
Classe TV:
Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do
canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de
faixas válidas.
"""


class TV:
    def __init__(self):
        self.numero_canal = 1
        self.volume = 0

    def trocar_canal(self, canal_novo: int):
        if 100 >= canal_novo >= 1:
            self.numero_canal = canal_novo
            print(f'Agora voce esta no canal {canal_novo}')
        else:
            print('Canal nao reconhecido')

    def aumentar_volume(self):
        if 99 >= self.volume >= 0:
            self.volume += 1
            print(f'Volume: {self.volume}')
        else:
            print(f'Volume: {self.volume}')

    def diminuir_volume(self):
        if 0 < self.volume <= 100:
            self.volume -= 1
            print(f'Volume: {self.volume}')
        else:
            print(f'Volume: {self.volume}')


if __name__ == '__main__':
    tv1 = TV()
    tv1.aumentar_volume()
    tv1.diminuir_volume()
    tv1.diminuir_volume()
    tv1.trocar_canal(13)
    tv1.trocar_canal(9)
