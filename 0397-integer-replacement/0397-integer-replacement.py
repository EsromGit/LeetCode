class Solution:
    def integerReplacement(self, n: int) -> int:
        cache = {}
        if n in cache:
            return cache[n]
    
        if n == 1:
            return 0
        
        if n % 2 == 0:
            value = 1+ self.integerReplacement(n //2)
        else:
            value = 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

        cache[n] = value
        return value