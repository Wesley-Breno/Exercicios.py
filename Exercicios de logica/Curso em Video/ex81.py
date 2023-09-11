"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

valores = []  # Lista onde ficara cada numero digitado
tem_valor_5 = False  # Variavel para saber se tem o valor 5 nos numeros digitados

print('\n\n\t\t\033[;37mDigite -1 pra parar de adicionar valores\033[m\n\n')

while True:  # Enquanto o usuario nao digitar -1
    valor = str(input('Digite o valor: '))

    if valor == '-1':  # Se for -1 a repeticao para e mostra o resultado
        break

    if valor.isdigit():  # Se o valor digitado for um numero
        valores.append(int(valor))

    else:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Digite um valor inteiro novamente.\n\n')

for numero in valores:
    if numero == 5:  # Se tiver o valor 5 nos valores digitados
        tem_valor_5 = '\033[;32mSim\033[m'

if tem_valor_5 is False:  # Se nao tiver nenhum valor 5 nos valores digitados
    tem_valor_5 = '\033[;31mNao\033[m'

print('\n\n\t\t\033[;1mResultado\033[m\n')
print(f'Total de valores digitados: {len(valores)}\n'
      f'Valores em ordem decrescente: {sorted(valores, reverse=True) if len(valores) > 0 else "Nao ha valor na lista"}\n'
      f'Tem valor 5 na lista: {tem_valor_5}\n\n')
