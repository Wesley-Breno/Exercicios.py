"""
Data com mês por extenso. Construa uma função que receba uma data no formato
DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""
from typing import Union

meses_com_31_dias = [1, 3, 5, 7, 8, 10, 12]
meses_com_30_dias = [4, 6, 9, 11]
todos_os_meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
meses_por_extenso = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]


def data_com_mes_por_extenso(data: str) -> Union[str, None]:
    """
    Funcao que recebe uma data no formata DD/MM/AAAA
    Valida a data e a retorna por extenso: DD de mes_por_extenso de AAAA
    Caso a data informada nao seja valida, a funcao ira retornar None.
    :param data: Data no formato DD/MM/AAAA que sera validada e retornada por extenso.
    :return: Retorna uma string com a data por extenso, ou retorna None se a data informada for invalida.
    """
    data_separada = data.split('/')
    data_valida = False

    # Se o formato da data estiver correto
    if len(data_separada) == 3:

        # Verificando se os valores informados sao numericos
        valores = []
        for valor in data_separada:
            if valor.isdigit():
                valores.append(valor)

        # Se todos os valores separados por '/' forem numericos.
        if len(valores) == 3:

            # Se mes informado estiver entre 1 e 12, e dias estiver entre 1 e 31
            if int(valores[1]) in todos_os_meses and 1 <= int(valores[0]) <= 31:
                index_mes = 0
                mes_por_extenso = ''

                # Pegando o mes informado por extenso
                for index, mes in enumerate(todos_os_meses):
                    if mes == int(valores[1]):
                        mes_por_extenso = meses_por_extenso[index]

                # Se for um mes com 30 dias
                if int(valores[1]) in meses_com_30_dias:
                    if 1 <= int(valores[0]) <= 30:  # Verificando se o dia esta entre 1 e 30
                        data_valida = True
                    else:
                        return None

                # Se for um mes com 31 dias
                elif int(valores[1]) in meses_com_31_dias:
                    if 1 <= int(valores[0]) <= 31:  # Verificando se o dia esta entre 1 e 31
                        data_valida = True
                    else:
                        return None

                # Se o mes for fevereiro
                else:
                    if int(valores[2]) % 4 == 0:  # Se for um ano bissexto
                        if 1 <= int(valores[0]) <= 29:  # Verificando se o dia esta entre 1 e 29
                            data_valida = True
                        else:
                            return None
                    else:
                        if 1 <= int(valores[0]) <= 28:  # Verificando se o dia esta entre 1 e 28
                            data_valida = True
                        else:
                            return None
            else:
                return None
        else:
            return None
    else:
        return None

    if data_valida:
        return f'{valores[0]} de {mes_por_extenso} de {valores[2]}'


if __name__ == '__main__':
    data_extenso = data_com_mes_por_extenso('1/8/2005')
    print(data_extenso)
