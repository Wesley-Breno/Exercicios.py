import re

texto = """
João trouxe     flores para sua amada namorada em 10 de janeiro de 1970.
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. maria, hoje sua esposa, ainda faz aquele
café com pão de queijo nas tardes de domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso pão de
queijo.
Não canso de ouvir a Maria:
""Jooooooãooooooooo, o café tá prontinho aqui. Veemm""!
Jã
"""

print(re.findall(r'jo+ão+', texto, flags=re.I))  # Mostrando os nomes 'joão', independente se tiver mais de 1 'o',
# mas precisa ter pelo menos 1.
print('-' * 25)

print(re.sub(r'jo+ão+', 'Felipe', texto,
             flags=re.I))  # Modificando o nome 'joão' para 'Felipe', independente da quantidade de 'o'.
print('-' * 25)

print(re.sub(r'jo*ão*', 'Felipe', texto, flags=re.I))  # Modificando 'joão' para 'Felipe', 'joão' pode não existir ou
# existir 1 vez ou varias vezes na string.
print('-' * 25)

print(re.sub(r'jo?ão?', 'Felipe', texto, flags=re.I))
print('-' * 25)

print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))  # Tenha no minimo um caractere 'o' ou mais.
print('-' * 25)
