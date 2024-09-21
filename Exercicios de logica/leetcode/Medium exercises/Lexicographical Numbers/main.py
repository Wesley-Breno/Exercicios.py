class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        lista = [str(p) for p in range(1, n+1)]
        lista_lexicografica = sorted(lista)
        response = [int(p) for p in lista_lexicografica]
        return response
