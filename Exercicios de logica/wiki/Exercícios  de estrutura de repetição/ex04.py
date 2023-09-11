"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.

pais_a + 3% = 82.400
pais_b + 1.5% = 203000
"""

pais_a = 80000  # Total de populacao do pais A
pais_b = 200000  # Total de populacao do pais B
total_de_anos = 0  # Variavel que ira conter o total de anos necessarios

while pais_a < pais_b:  # Enquanto o pais A for menor que o pais B
    pais_a = pais_a + (pais_a * 3 / 100)  # Adicionando 3% da população anual do pais A
    pais_b = pais_b + (pais_b * 1.5 / 100)  # Adicionando 1.5% da população anual do pais B
    total_de_anos += 1  # Fazendo a contagem de anos

print(f"""\n\n\t\tResultado de anos

Sera necessario {total_de_anos} anos para o pais A ultrapassar o pais B.""")
