class Solution:
    def __init__(self):
        self.cache = {}

    def integerReplacement(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
    
        if n == 1:
            return 0
        
        if n % 2 == 0:
            value = 1+ self.integerReplacement(n //2)
        else:
            value = 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

        self.cache[n] = value
        return value