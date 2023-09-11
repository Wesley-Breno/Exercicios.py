class Numeros:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __add__(self, other):  # Pegando cada valor de cada objeto e retornando a soma entre eles.
        return (self.n1 + self.n2) + (other.n1 + other.n2)

    def __gt__(self, other):  # Verificando se os valores do primeiro objeto sao maiores que o segundo objeto.
        if (self.n1, self.n2) > (other.n1, other.n2):
            return True
        else:
            return False

    def __lt__(self, other):  # Verificando se os valores do primeiro objeto sao menores que o segundo objeto.
        if (self.n1, self.n2) < (other.n1, other.n2):
            return True
        else:
            return False

    def __eq__(self, other):  # Verificando se os valores do primeiro objeto sao iguais ao do segundo objeto.
        if (self.n1, self.n2) == (other.n1, other.n2):
            return True
        else:
            return False


num1 = Numeros(2, 2)
num2 = Numeros(2, 2)

soma = num1 + num2
print('\nA soma de cada valor em cada objeto equivale a:', soma)

print('O objeto 1 é maior que o objeto 2? -> ', num1 > num2)
print('O objeto 1 é menor que o objeto 2? -> ', num1 < num2)
print('O objeto 1 é igual ao objeto 2? -> ', num1 == num2)
