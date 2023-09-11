from threading import Thread  # Classe que sera usada para realizar o thread da funcao 'carro'


def carro(velocidade: float, piloto: str) -> None:
    """
    Funcao que simula uma corrida ate chegar no trajeto 100.
    :param velocidade: Velocidade que o piloto ira correr ate chegar no trajeto 100.
    :param piloto: Nome do piloto.
    :return: None
    """

    trajeto = 0

    while trajeto <= 100:  # Enquanto o piloto nao chegar no trajeto 100
        print(f'Carro de {piloto}: {trajeto} ')
        trajeto += velocidade

    print(f'{piloto} CHEGOU AO DESTINO!')


# Apostando corrida entre 2 pilotos (threads da mesma funcao)
car1 = Thread(target=carro, args=(10, 'werli')).start()
car2 = Thread(target=carro, args=(10, 'jessica')).start()
