class Solution:
    def capitalizeTitle(self, title: str) -> str:
        new_title = ''
        for word in title.split():
            if len(word) <= 2:
                new_title += ' ' + word.lower()
                continue
            new_title += ' ' + word.capitalize()

        return new_title.strip()