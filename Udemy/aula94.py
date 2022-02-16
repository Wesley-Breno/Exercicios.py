# Faca um validador de CNPJ usando o calculo mostrado na aula 94.

from functions import titulo, erro, programa_encerrado, pular, press_enter    # Funcoes que criei


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


titulo('Validar CNPJ')
press_enter('para comecar.')

while True:
    try:
        print(f'\n\n\033[;37m{"Digite [ 0 ] para encerrar.":^45}\033[m\n')
        cnpj = str(input('Informe o CNPJ: '))
    except:
        erro('Por favor, tente novamente.')
        pular(5)
    else:
        if cnpj == '0':    # Se o usuario digitar 0 o programa encerra.
            break
        else:
            try:
                cnpj = numeros_cnpj(cnpj)    # Pegando somente os numeros do CNPJ.
            except:
                erro('Algo esta errado.\nInforme o CNPJ novamente.')
                pular(5)
            else:
                try:
                    cnpj_copia = numeros_cnpj(cnpj, 1)    # Pegando todos os numeros menos os 2 ultimos.
                    cnpj_copia = ultimo_ou_penultimo_digito(cnpj_copia)    # Fazendo o calculo e pegando o penultimo numero.
                    cnpj_copia = ultimo_ou_penultimo_digito(cnpj_copia, 1)    # Fazendo o calculo e pegando o ultimo numero.
                except:
                    erro('Algo esta errado.\nInforme o CNPJ novamente.')
                    pular(5)
                else:
                    if cnpj_copia == cnpj:    # Se o CNPJ que o usuario digitou for igual ao calculo usado para validar.
                        print(f'\n\n\033[;1m{"Este CNPJ é valido.":^45}\033[m\n')
                        press_enter('para validar novamente.')
                    else:
                        print(f'\n\n\033[;1m{"Este CNPJ é invalido.":^45}\033[m\n')
                        press_enter('para validar novamente.')

programa_encerrado()    # Mensagem de despedida para o usuario.
