r"""
\w -> [a-zA-Z0-9À-ú]
\d -> [0-9]
\s -> Pegando os espacos em brancos, virgulas e quebra de linhas (\n).
\b -> Bordas

(Ao colocar o shorthand em maiusculo voce ira fazer o contrario da ação)
"""

import re

texto = """
João trouxe     flores para sua amada namorada em 10 de janeiro de 1970, Maria era o nome dela.

Foi um ano excelente na vida de joão. teve 5 filhos, todos adultos atualmente. maria, hoje sua esposa, ainda faz aquele
café com pão de queijo nas tardes de domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooãooooooo, o café tá prontinho aqui. Veeemm"!
"""

print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))  # Pegando todos os tipos de caracteres possiveis
print(re.findall(r'\w+', texto))  # Fazendo a mesma coisa do codigo acima, porem usando o shorthand \w.

print(re.findall(r'[0-9]+', texto))  # Pegando todos os numeros de 0 a 9
print(re.findall(r'\d+', texto))  # Fazendo a mesma coisa do codigo acima, porem usando o shorthand \d

print(re.findall(r'\s+', texto))  # Pegando os espacos em brancos, virgulas e quebra de linhas (\n).

print(re.findall(r'\bflo\w+', texto))  # Pegando todas as palavras que comecem com 'flo'.

print(re.findall(r'\w+es\b', texto))  # Pegando todas as palavraas que terminam com 'es'.

print(re.findall(r'\b\w{4}\b', texto))  # Pegando todos os conjuntos de caracteres que tenham apenas 4 caracteres.
