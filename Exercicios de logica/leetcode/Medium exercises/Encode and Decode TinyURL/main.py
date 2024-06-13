from string import ascii_lowercase
from random import choice


class Codec:
    def __init__(self):
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        shorturl = ''
        for c in range(int(len(longUrl) / 4)):
            shorturl += choice(ascii_lowercase)

        https, site = longUrl.split('/')[0], longUrl.split('/')[2]
        self.urls[longUrl] = https + '//' + shorturl + '.com'
        return self.urls[longUrl]

    def decode(self, shortUrl: str) -> str:
        for key, value in self.urls.items():
            if value == shortUrl:
                return key

