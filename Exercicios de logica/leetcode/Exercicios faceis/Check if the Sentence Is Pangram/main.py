class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for letter in string.ascii_lowercase:
            try:
                sentence.index(letter)
            except ValueError:
                return False
        return True
