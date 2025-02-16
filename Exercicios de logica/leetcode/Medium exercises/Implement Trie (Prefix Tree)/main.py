class Trie:
    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        self.tree[word] = True

    def search(self, word: str) -> bool:
        try:
            return self.tree[word]
        except KeyError:
            return False

    def startsWith(self, prefix: str) -> bool:
        words = self.tree.keys()
        for word in words:
            if str(word).startswith(prefix):
                return True
        return False