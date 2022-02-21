# Fazendo um gerador de CNPJs com o calculo da aula passada.

from functions import titulo, press_enter, programa_encerrado, pular, encerrar    # Funcoes que criei.
from random import randint    # Importacao para pegar numeros inteiros aleatorios.


def numeros_cnpj(cnpj, todos_numeros=0):
    """
    funcao para tirar os [ / ] e [ . ] e deixar somente os numeros
    tirando o penultimo e ultimo ou deixando tudo completo.
    :param cnpj: parametro onde ficara o CNPJ.
    :param todos_numeros: se esse parametro receber 0, vai deixar todos os numeros, 1 para tirar o ultimo e penultimo.
    :return: retorna somente os numeros do CNPJ, caso a quantidade de caracteres nao esteja certa, retorna False.
    """
    if todos_numeros == 0:    # Deixando todos os numeros.
        cnpj_copia = ''    # Variavel onde vai ficar so os numeros do CNPJ.

        cont = 0    # Contador para saber a hora que o programa pegou todos os numeros, menos os 2 ultimos.
        for c in cnpj:
            if cont == 14:
                break
            if c.isnumeric():    # Pegando so os caracteres que sao numeros.
                cnpj_copia += c
                cont += 1

        if len(cnpj_copia) == 14:    # Se o CNPJ ter o tamanho do caractere normal de um CNPJ (14 todos os numeros, 12 todos os numeros menos os 2 ultimos.)
            return cnpj_copia
        else:    # CNPJ invalido
            return False

    if todos_numeros == 1:    # Deixando os numeros, mas tirando os 2 ultimos.
        cnpj_copia = ''  # Variavel onde vai ficar so os numeros do CNPJ.

        cont = 0  # Contador para saber a hora que o programa pegou todos os numeros, menos os 2 ultimos.
        for c in cnpj:
            if cont == 12:
                break
            if c.isnumeric():  # Pegando so os caracteres que sao numeros.
                cnpj_copia += c
                cont += 1

        if len(cnpj_copia) == 12:
            return cnpj_copia
        else:
            return False


def ultimo_ou_penultimo_digito(cnpj, ultimo_ou_penultimo=0):
    """
    Funcao para pegar o ultimo ou o penultimo numero, usando o calculo
    para mostrado na aula para isso.
    :param cnpj: Parametro onde fica o CNPJ
    :param ultimo_ou_penultimo: recebe 0, se for o penultimo numero, rebece 1 se for ultimo.
    :return: Retorna o cnpj com o ultimo/penultimo numero.
    """
    if ultimo_ou_penultimo == 0:    # Pegando o penultimo numero.
        cont = 5    # Contador que sera usado para fazer a multiplicacao.
        soma = 0    # Soma da multiplicacao
        numeros_multiplicados = []    # numeros multiplicados, listados para depois somar.

        for n in cnpj:    # Multiplicando o numero do CNPJ da vez, e usando o contador pra isso.
            if cont == 1:    # Se o contador chegar a querer multiplicar por 1, contador recebe 9 e multiplica novamente
                cont = 9
            numeros_multiplicados.append(int(n) * cont)
            cont -= 1

        for n in numeros_multiplicados:
            soma += n

        calculo = 11 - (soma % 11)    # Calculo para pegar o penultimo/ultimo numero do CNPJ.
        penultimo_numero = calculo
        if calculo > 9:    # Se o penultimo/ultimo numero for maior que 9, ele vai receber 0, conforme dito na aula.
            penultimo_numero = 0
            return cnpj + str(penultimo_numero)    # Concatenando o ultimo/penultimo numero do calculo com o restante do CNPJ.
        else:
            return cnpj + str(penultimo_numero)

    if ultimo_ou_penultimo == 1:    # Pegando o penultimo numero.
        cont = 6    # Comecando com o contador 6, porque o penultimo numero foi adicionado.
        soma = 0
        numeros_multiplicados = []

        for n in cnpj:
            if cont == 1:
                cont = 9
            numeros_multiplicados.append(int(n) * cont)
            cont -= 1

        for n in numeros_multiplicados:
            soma += n

        calculo = 11 - (soma % 11)
        ultimo_numero = calculo
        if calculo > 9:
            ultimo_numero = 0
            return cnpj + str(ultimo_numero)
        else:
            return cnpj + str(ultimo_numero)


titulo('Gerador de CNPJs')
press_enter('para gerar um CNPJ.')

deseja = ''    # Varivel onde ficara a decisao do usuario, se ele quer ou nao encerrar o programa.
while deseja != 1:    # Enquanto o usuario nao desejar encerrar.
    numeros = ''    # Variavel onde ficara o CNPJ
    numeros_copia = ''    # Copia do CNPJ
    for c in range(0, 14):    # Pegando 14 numeros aleatorios para ser o CNPJ.
        numeros += str(randint(0, 9))

    numeros_copia = numeros_cnpj(numeros, 1)    # Pegando todos os numeros, menos os 2 ultimos
    numeros_copia = ultimo_ou_penultimo_digito(numeros_copia)    # Fazendo o calculo e pegando o penultimo numero.
    numeros_copia = ultimo_ou_penultimo_digito(numeros_copia, 1)    # Fazendo o calculo e pegando o ultimo numero.

    if numeros_copia == numeros:    # Se apos o calculo, os numeros forem iguais, o CNPJ é valido.
        cnpj_com_pontuacao = ''    # Variavel onde ficara o CNPJ com as pontuacoes e etc.
        cont = 0    # Contador para saber onde o for esta e assim poder adicionar as pontuacoes no lugar certo.
        for n in numeros:
            if cont == 2:
                cnpj_com_pontuacao += '.'
            if cont == 5:
                cnpj_com_pontuacao += '.'
            if cont == 8:
                cnpj_com_pontuacao += '/'
            if cont == 12:
                cnpj_com_pontuacao += '-'
            cnpj_com_pontuacao += n
            cont += 1

        pular(2)
        print('--' * 16)
        print(f'CNPJ gerado: \033[;1m{cnpj_com_pontuacao}\033[m')
        print('--' * 16)
        press_enter()
        deseja = encerrar()    # Perguntando ao usuario se ele deseja encerrar o programa.
        if deseja == 0:    # Se o usuario nao quiser encerrar o programa, o programa ira pular 5 linhas.
            pular(5)


programa_encerrado()    # Mensagem de despedida para o usuario.
