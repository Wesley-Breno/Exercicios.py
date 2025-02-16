numbers_letters = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

from itertools import combinations

digits = "23"

lista = []

for key, value in numbers_letters.items():
    if key in digits:
        lista += value

print(lista)

combs = combinations([['a', 'b', 'c'], ['d', 'e', 'f']], len(digits))
for comb in combs:
    print(comb)
