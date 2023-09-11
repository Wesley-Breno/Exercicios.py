"""
Crie uma função1 que recebe uma função2 como parametro e retorne o valor
da função2 executada. Faça a função1 executar duas funçoes que recebam
um numero diferente de argumentos.
"""


def mestre(funcao, *args, **kwargs):  # Função mestre onde vai receber a função2 e seus argumentos.
    return funcao(*args, **kwargs)  # Retornando a função2 e seus argumentos


def fala_oi(nome):
    return f'Oi, {nome}'


def saudacao(nome, saudar):
    return f'{saudar}, {nome}'


executar = mestre(fala_oi, 'Luiz')  # Escolhendo a função 'fala_oi', e mandando o argumento 'Luiz'.
executar2 = mestre(saudacao, saudar='bom diaaa', nome='Werli')  # Escolhendo a função 'saudacao', e usando os kwargs para ser especifico no valor que cada parametro vai receber.

print(executar)
print(executar2)
