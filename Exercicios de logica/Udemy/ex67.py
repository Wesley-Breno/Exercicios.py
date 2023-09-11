"""
lista = [string[n:n + 10] for n in range(0, len(string), 10)]

    Vai fazer uma contagem de 0 ate quantos caracteres tiver a variavel 'string'
    pulando de 10 em 10, para poder usar o 'string[n:n + 10]' por quê ai ele ira
    retornar sempre do 0 ate o 9, separando os numeros.

retorno = '.'.join(lista)

    Vai juntar cada elemento da 'lista' e colocar um '.' entre eles.
"""

string = '0123456789012345678901234567890123456789'
lista = [string[n:n + 10] for n in range(0, len(string), 10)]
retorno = '.'.join(lista)
