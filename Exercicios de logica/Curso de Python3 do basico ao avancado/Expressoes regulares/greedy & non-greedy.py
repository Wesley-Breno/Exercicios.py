"""
Greedy e non-greedy

    Essas palavras significam basicamente um quantificador...

        'guloso' -> Greedy
        'nao guloso' -> Non-greedy

    Guloso:
        O guloso pode significar quando o quantificador continua verificando os caracteres da string, mesmo depois de
        ele ja ter achado oque queria, deixando assim o retorno da lista com apenas um item/dado.

    Nao guloso:
        O nao guloso significa quando o quantificador para de verificar os caracteres da string depois que ele acha oque
        queria, ou seja, apos ele achar oque quer, ele ira considerar a proxima ocorrencia como outro item/dado da lista
        que sera adicionado.
"""

import re
texto = """
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
"""

print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))  # Exemplo de quantificador 'guloso'.

print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto))  # Exemplo de um quantificador 'nao guloso'.
