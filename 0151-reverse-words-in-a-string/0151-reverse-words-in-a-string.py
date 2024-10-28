class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        ans = ' '.join(lst[::-1])
        return ans