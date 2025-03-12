class Solution:
    def getRLE(self, numbers: str) -> str:
        cache = []
        rle = ''
        for i, num in enumerate(numbers):
            if num in cache or len(cache) == 0:
                cache.append(num)
                if i == len(numbers)-1:
                    rle += str(cache.count(cache[0])) + cache[0]
                    cache.clear()
            else:
                rle += str(cache.count(cache[0])) + cache[0]
                cache.clear()
                if i == len(numbers)-1:
                    rle += '1' + num
                    continue
                cache.append(num)
        return rle

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        next_rle = '1'
        for _ in range(1, n):
            next_rle = self.getRLE(next_rle)
        return next_rle