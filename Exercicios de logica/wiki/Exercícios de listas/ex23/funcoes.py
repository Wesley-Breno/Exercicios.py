"""
Funcoes para se usar no programa principal
"""


def converter_bytes_para_megabytes(bytes_para_converter):
    return float(f'{bytes_para_converter / 1000000:.2f}')


def percentual_de_uso_do_usuario(megabytes_usados_usuario, total_megabytes_equipe):
    return float(f'{megabytes_usados_usuario / total_megabytes_equipe * 100:.2f}')
