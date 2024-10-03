class Solution:
    def __init__(self):
        self.memo = {}

    def integerReplacement(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
    
        if n == 1:
            return 0
        
        if n % 2 == 0:
            value = 1+ self.integerReplacement(n //2)
        else:
            value = 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

        self.memo[n] = value
        return value