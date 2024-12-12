class MinStack:
    def __init__(self):
        self.pilha = []

    def push(self, val: int) -> None:
        self.pilha.insert(0, val)

    def pop(self) -> None:
        self.pilha.pop(0)

    def top(self) -> int:
        return self.pilha[0]

    def getMin(self) -> int:
        return min(self.pilha)
