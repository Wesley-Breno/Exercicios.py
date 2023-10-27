class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        response = []

        for c in range(1, n + 1):
            if c % 3 == 0 and c % 5 == 0:
                response.append('FizzBuzz')
                continue
            elif c % 3 == 0:
                response.append('Fizz')
                continue
            elif c % 5 == 0:
                response.append('Buzz')
                continue
            response.append(str(c))
        
        return response