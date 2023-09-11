import re

texto = """
João trouxe     flores para sua amada namorada em 10 de janeiro de 1970.
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. maria, hoje sua esposa, ainda faz aquele
café com pão de queijo nas tardes de domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso pão de
queijo.
Não canso de ouvir a Maria:
""Jooooooâooooooooo, o café tá prontinho aqui. Veemm""!
"""

print(re.findall(r'joão|MARIA', texto,
                 flags=re.I))  # Mostrando os nomes 'joão' e 'maria' independente se estiverem maiusculo ou nao.

print(re.findall(r'adultos|.oão|.aria',
                 texto))  # O . pode ser qualquer caractere, mas tem que ter os restantes dos caracteres já que não
# são pontos.

print(re.findall(r'[Jj]o[aãAÃ]o|[Mm]aria',
                 texto))  # Os colchetes servem para especificar quais letras podem estar no local da string.

print(re.findall(r'[a-zA-Z0-9]oão|[a-zA-Z]aria',
                 texto))  # Especificando que a primeira letra pode estar entre 'a' e 'z', 'A' e 'Z' so que
# maiusculo, ou pode ser um numero de 0 a 9.

print(re.findall(r'joão|MARIA', texto,
                 flags=re.I))  # Colocando um parametro a mais e informando que não importa se a letra estiver em
# maiuscula ou minuscula.

